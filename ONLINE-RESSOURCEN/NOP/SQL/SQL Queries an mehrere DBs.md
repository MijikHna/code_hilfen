z.B wenn man SaaS für mehrere Kunden betreibt. Jeder Kunde hat dann eigene DB. Wenn man aber etwas aus allen DBs fragen will:
1. Views = alle Tabellen in einer View vereinen: (SuBD-Tool von SQL)
```sql
CREATE VIEW sample_table AS (
  SELECT "tenant_1" AS tenant, t.* FROM tenant_1.sample_table AS t
  UNION ALL
  SELECT "tenant_2" AS tenant, t.* FROM tenant_2.sample_table AS t
  ...  
  UNION ALL
  SELECT "tenant_N" AS tenant, t.* FROM tenant_N.sample_table AS t
)
```
* `tenant_X` - DB-Name
* dann muss man mit `JOIN`-Abfragen vorsichtig sein, da da auch diese Syntax gilt:
```sql
SELECT 
    pp.tenant, pp.name, ppg.num
FROM
    products__products AS pp LEFT JOIN products__product_gtins AS ppg ON (pp.id = ppg.product_id AND pp.tenant = ppg.tenant)
```
2. damit man nicht immer langen Queries eingeben muss kann man SQL-Prozeduren schrieben:
    1. Prozedur um eine Tabelle für alle DB machen:
        * Code:
        ```sql
        CREATE PROCEDURE `update_table_view`(IN tbl_name VARCHAR(100), IN db_pattern_re VARCHAR(100))
        BEGIN
            DECLARE all_dbs_view LONGTEXT;
            DECLARE all_dbs_done INT DEFAULT 0;
            DECLARE all_dbs_indx INT DEFAULT 0;
            DECLARE cur_tenant_db VARCHAR(100);

            -- (A)
            DECLARE all_dbs_cur CURSOR FOR SELECT `schema_name` FROM information_schema.schemata WHERE `schema_name` REGEXP db_pattern_re;
            DECLARE CONTINUE HANDLER FOR NOT FOUND SET all_dbs_done = 1;

            -- (B)
            SET all_dbs_view = CONCAT("CREATE VIEW ", tbl_name, " AS ");

            SET all_dbs_done = 0;
            SET all_dbs_indx = 0;

            -- (C)
            OPEN all_dbs_cur;
            all_dbs_loop: LOOP
                FETCH all_dbs_cur INTO cur_tenant_db;
                IF all_dbs_done = 1 THEN LEAVE all_dbs_loop; END IF;

                -- (D)
                IF all_dbs_indx > 0 THEN SET all_dbs_view = CONCAT(all_dbs_view, " UNION ALL "); END IF;
                SET all_dbs_view = CONCAT(all_dbs_view, "SELECT \"", cur_tenant_db, "\" AS tenant, t_", all_dbs_indx, ".* FROM `", cur_tenant_db, "`.`", tbl_name, "` AS t_", all_dbs_indx);
                SET all_dbs_indx = all_dbs_indx + 1;

            END LOOP all_dbs_loop;
            CLOSE all_dbs_cur;

            -- (E)
            SET @drop_view = CONCAT("DROP VIEW IF EXISTS ", tbl_name);
            PREPARE drop_view_stm FROM @drop_view; EXECUTE drop_view_stm; DEALLOCATE PREPARE drop_view_stm;

            -- (F)
            SET @all_dbs_view_v = all_dbs_view;
            PREPARE all_dbs_view_stm FROM @all_dbs_view_v; EXECUTE all_dbs_view_stm; DEALLOCATE PREPARE all_dbs_view_stm;
        END
        ```
        * diese Prozedur hat zwie Parameter: `tbl_name` und `db_patter_re`
        1. A) = Сначала надо объявить курсор для итеративного обхода всех БД, включённых в представление. Чтобы отфильтровать только те БД, которые нам нужны, используем регулярное выражение db_pattern_re. Обработчик CONTINUE HANDLER позаботится о том, чтобы цикл остановился после итеративного обхода всех найденных БД.
        2. B) = Инициализируем переменную all_dbs_view, содержащую нашу полную инструкцию CREATE VIEW. Переменная может оказаться довольно длинной (LONGTEXT), в зависимости от числа прошедших фильтрацию БД.
        3. C) = Теперь открываем курсор и начинаем итеративный обход каждой прошедшей фильтрацию БД. Оператор IF выполнит проверку на наличие переменной all_dbs_done на каждом этапе. При запуске обработчика CONTINUE HANDLER переменная будет иметь значение 1.
        4. D) = Первая итерация не требует ставить в начало UNION ALL, а вот все последующие будут ставить. Следующая строчка конкатенирует, то есть добавляет текущий оператор SELECT, содержащий все записи из таблицы БД конкретного пользователя: `SELECT "tenants_DB" AS tenant, t.* FROM tenants_DB.some_table AS t`
        5. E) Прежде чем создавать VIEW, необходимо убедиться, что предыдущее (если оно существовало) удалено.
        6. F) И, наконец, запускаем саму инструкцию, создающую VIEW.
        * Prozedur aufrufen: `CALL update_table_view("sample_table", "tenant_[0-9]+");`
    2. Prozedur um alle Tabellen durchzulaufen
        * Code: 
        ```sql
        CREATE PROCEDURE `update_all_views`(IN db_first VARCHAR(100), IN db_pattern_re VARCHAR(100))
        BEGIN
            DECLARE all_tbls_done INT DEFAULT 0;
            DECLARE cur_tbl VARCHAR(100);

            -- A
            DECLARE all_tbls_cur CURSOR FOR SELECT `table_name` FROM information_schema.tables WHERE table_schema = db_first;
            DECLARE CONTINUE HANDLER FOR NOT FOUND SET all_tbls_done = 1;

            SET all_tbls_done = 0;
            OPEN all_tbls_cur;
            -- B
            all_tbls_loop: LOOP
                FETCH all_tbls_cur INTO cur_tbl;
                IF all_tbls_done = 1 THEN LEAVE all_tbls_loop; END IF;

                -- C
                CALL update_table_view(cur_tbl, db_pattern_re);

            END LOOP all_tbls_loop;
            CLOSE all_tbls_cur;
        END
        ```
        1. A) Объявляем курсор для итеративного обхода всех таблиц, найденных в базе данных db_first. Обработчик CONTINUE HANDLER позаботится о том, чтобы цикл остановился после итеративного обхода всех обнаруженных таблиц.
        2. B) Открываем курсор и начинаем итеративный обход каждой найденной таблицы. Оператор IF выполнит проверку на наличие переменной all_tbls_done на каждом этапе. При запуске обработчика CONTINUE HANDLER переменная будет иметь значение 1.
        3. C) Получив значение текущей таблицы, хранимой в переменной cur_tbl, можно выполнить хранимую процедуру, которая создаст VIEW специально для cur_tbl.При выполнении хранимой процедуры: `CALL update_all_views("tenant_1", "tenant_[0-9]+");` => Ausgabe: alle Tabellen aus DB `tenant_1`,
* Mögliche Errors
    1. `Prepared statement needs to be re-prepared`=> `SET GLOBAL table_definition_cache = 2800;` eventuell 2800 ändern
    2. `Illegal mix of collations (utf8mb4_general_ci,COERCIBLE) and (utf8mb4_unicode_ci,IMPLICIT) for operation ‘=’` => Codierung ändern: `SELECT CONVERT("tenants_DB" USING utf8mb4) AS tenant, t.* FROM tenants_DB.some_table AS t`