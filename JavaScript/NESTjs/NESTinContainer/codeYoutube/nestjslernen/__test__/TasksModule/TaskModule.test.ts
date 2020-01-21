import { Test } from '@nestjs/testing';
import { TasksService } from '../../src/tasks/tasks.service';
import { TaskStatus } from '../../src/tasks/tasks.model';
import { TasksRepository } from '../../src/tasks/tasks.repository';
import { GetTasksFilterDto } from '../../src/tasks/get-tasks-filte.dto';

const mockUser = { username: "Max" };
const mockTaskRepository = () => ({
    getTasks: jest.fn(), //Funktion, die simuliert werden soll; <= getTask-Method ist vom Typ jest.fn() = MockMethode
}); //Objekt, der TaskRepository simulieren soll; ({}) = Objekt direkt returnen; 

describe("TaskService", () => {
    let tasksService; //was getestet wird
    let tasksRepo; //was TaskService selbst benutzt (sollte im constructor stehen)

    beforeEach(async () => {
        const module = await Test.createTestingModule({
            providers: [
                TasksService,
                { provide: TasksRepository, useFactory: mockTaskRepository }, // hier Mock verwenden, da z.B man nicht will das wirklcih sich mit DB verbindet => über Mock TaskRepository simulieren; hier kann man useFactory/Class/Value -> hier Factory damit es jedes Mal neu ertellt wrid; <- hier wird an mockTaskRepository gesagt, welches Objekt genau simuliert werden soll
            ],
        }).compile(); //Module zum Testen erstellen; await, da compile-Funktion async ist

        tasksService = await module.get<TasksService>(TasksService);
        tasksRepo = await module.get<TasksRepository>(TasksRepository);
    })

    //getTask(filterDto: GetTasksFilterDto, user: User)
    describe("getTasks", () => {
        it("gets all tasks form repo", async () => {
            //taskRepository.getTasks.mockResolvedValue();
            //taskRepository.getTasks.mockReturnValue();
            //taskRepository.getTasks.mockRejectedValue();
            tasksRepo.getTasks.mockResolvedValue("someValue"); //sagt man welchenWert es returnen soll

            expect(tasksRepo.getTasks).not.toHaveBeenCalled();

            const filters: GetTasksFilterDto = { status: TaskStatus.IN_PROGRESS, search: "Some search query" };
            const result = await tasksService.getTasks(filters, mockUser);
            expect(tasksRepo.getTasks).toHaveBeenCalled();
            expect(result).toEqual("someValue");
        })
    })
});