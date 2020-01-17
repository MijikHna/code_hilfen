// import { Test, TestingModule } from '@nestjs/testing';
// import { BooksService } from './books.service';

// describe('BooksService', () => {
//   let service: BooksService;

//   beforeEach(async () => {
//     const module: TestingModule = await Test.createTestingModule({
//       providers: [BooksService],
//     }).compile();

//     service = module.get<BooksService>(BooksService);
//   });

//   it('should be defined', () => {
//     expect(service).toBeDefined();
//   });
// });

import { Test, TestingModule } from "@nestjs/testing";
import { BooksController } from "../../src/books/books.controller";
import { BooksService } from "../../src/books/books.service";

describe('BooksController', function () {

  let booksController: BooksController;
  let booksService: BooksService;

  beforeEach(async () => {
    const module = await Test.createTestingModule({
      controllers: [BooksController],
      providers: [BooksService],
    }).compile();

    booksService = module.get<BooksService>(BooksService);
    booksController = module.get<BooksController>(BooksController);
  });

  describe('getBooks', function () {
    test("Test einfach so", function () {
      const result: String = "test";
      expect("test").toBe(result);
    });
  });
});