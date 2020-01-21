import { Task } from './task.entity';
import { BaseEntity, Entity, PrimaryGeneratedColumn, EntityRepository, Repository } from 'typeorm';

@EntityRepository(Task)
export class TasksRepository extends Repository<Task>{
    //hier kommt Logik
} 
