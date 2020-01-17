import { Test, TestingModule } from "@nestjs/testing";
import { BooksController } from "../src/books/books.controller";
import { BooksService } from "../src/books/books.service";

describe('BooksController', function () {

    let booksController: BooksController;
    let booksService: BooksService;

    beforeEach(async () => {
        const module: TestingModule = await Test.createTestingModule({
            controllers: [BooksController],
            providers: [BooksService],
        }).compile();

        booksService = module.get<BooksService>(BooksService);
        booksController = module.get<BooksController>(BooksController);
    });

    describe('getBooks', () => {
        it('should return an array of cats', async () => {
            let result: any;
            jest.spyOn(booksService, 'getBooks').mockImplementation(() => result);

            expect(await booksController.getBooks()).toBe(result);
        });
    });
});