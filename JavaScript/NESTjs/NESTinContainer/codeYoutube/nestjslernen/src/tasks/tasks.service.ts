import { Injectable } from '@nestjs/common';
import { Task, TaskStatus } from './tasks.model';

import * as uuid from 'uuid/v1'
import { CreateTaskDto } from './create-task.dto';

@Injectable()
export class TasksService {
    [x: string]: any;
    private tasks: Task[] = []; //nur Temporär,da noch keine DB

    getAllTasks(): Task[] { //damit kann der Controller auf TaskService-Sachen zugreifen
        return this.tasks;
    }

    createTask(title: string, desc: string): Task {
        const task: Task = {
            id: uuid(),
            title, //in ES6 wenn Name + VariableName im Scope gleich => JS macht alles selbst ~ this.title = title
            desc,
            status: TaskStatus.OPEN,
        }

        this.tasks.push(task);
        return task; //returnen, damit im Frontend entschieden werden kann was + wie damit weiterverfahren wird
    }

    createTask02(createTaskDto: CreateTaskDto): Task {
        const { title, desc } = createTaskDto; //DTO in primitive Variablen entpacken

        const task: Task = {
            id: uuid(),
            title,
            desc,
            status: TaskStatus.OPEN,
        }

        this.tasks.push(task);
        return task; //returnen, damit im Frontend entschieden werden kann was + wie damit weiterverfahren wird
    }

    getTaskById(id: string): Task {
        //es gibt mehrere Möglichkeiten das zu realisieren
        return this.tasks.find(task => {
            task.id === id
        });
    }

    deleteTask(id: string): void {
        //Es gibt mehrere Möglichkeiten die zu realisieren
        //Hier wird Array-filter()-Methode verwendet verwendet
        this.task = this.task.fitler(task => task.id != id); //der Code nach => wird auf ganzes Array angewendet und wenn false wird return => dieser Task wird returt
    }

    updateTaskStatus(id: string, status: TaskStatus) {
        const task = this.getTaskById(id);
        task.status = status;
        return status;
    }
}
