import { Injectable } from '@nestjs/common';

@Injectable()
export class EventsService {
    findAll(): any[] {
        return [
            {
                id: 1,
                name: "Angular.DE Intensiv Schulung",
            },
            {
                id: 2,
                name: "Das ist nur ein Test",
            },
            {
                id: 3,
                name: "Das ist der zweite Test",
            },
        ];
    }
}
