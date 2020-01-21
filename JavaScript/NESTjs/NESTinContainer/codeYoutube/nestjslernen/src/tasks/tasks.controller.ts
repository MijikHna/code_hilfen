import { Controller, Get, Post, Body, Param, Delete, Patch } from '@nestjs/common';
import { TasksService } from './tasks.service';
import { Task, TaskStatus } from './tasks.model';
import { CreateTaskDto } from './create-task.dto';

@Controller('tasks')

export class TasksController {
    [x: string]: any;
    private taskService: TasksService;


    constructor(taskService: TasksService) {
    }

    @Get()
    getAllTasks() { //diese Funktion wird aufgerufen, wenn REST-Api GET: localhost aufruft
        this.taskService.getAllTasks();
    }

    @Post()
    createTask01(@Body() body) {
        console.log("body", body);
    }

    @Post()
    createTask(
        @Body("title") title: string,
        @Body("desc") desc: string,
    ): Task {
        //console.log("title", title);
        //console.log("desk", desk);
        return this.taskService.createTask(title, desc);
    }

    @Post()
    createTask03(@Body() createTaskDto: CreateTaskDto): Task {
        //console.log("title", title);
        //console.log("desk", desk);
        return this.taskService.createTask02(createTaskDto);
    }

    @Get('/:id') //auf / kann man auch verzichten
    getTaskById(@Param('id') id: string) {
        return this.taskService.getTaskById(id);
    }

    @Delete('/:id')
    deleteTask(@Param('id') id: string): void {
        this.tasksService.deleteTask(id);
    }

    @Patch('/:id/status')
    updateTaskStatus(@Param('id') id: string, @Body('status') status: TaskStatus) {
        return this.taskService.updateTaskStatus(id, status)
    }
}
