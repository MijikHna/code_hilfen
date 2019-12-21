import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return '<h1>Hello World!</h1> <h2>Test Debugger</h2> <h3>Test Debugger</h3> <h3>Test Debugger</h3>';
  }
}
