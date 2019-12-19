import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return '<dev><h1>Hello World! und Test 03</h1></dev><h2>Test Haha</h2><h3>Test</h3> <h3>Test</h3>';
  }
}
