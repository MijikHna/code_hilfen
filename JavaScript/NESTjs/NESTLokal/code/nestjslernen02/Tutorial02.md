**https://scotch.io/tutorials/getting-started-with-nestjs#toc-installing-nest-js**

### Overview of Nest.js
* Vorteile von Nest.js
    * it surrounds your route handler body with try..catch blocks
    * it makes every route handler async
    * it creates a global express router
    * it creates a separated router for each controller
    * it binds error-handling middleware
    * it binds body-parser middleware (both json and extended urlencoded)
### Building blocks of Nest.js
### Controllers:
    * behandeln Requests und returnen Response
    * Routing Mechanismus kann richtigen Controller dem richtigem Request zuweisen
    * werden mit Docorator `@Controller` markiert
    * `@Controller("users")` = Controller für `\users\`
    * Controller müssen einem Modul hinzugefügt werden z.B Root-Modul `ApplicationModule` (`application.module.ts`)
### Providers
* 
