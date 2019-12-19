import { Injectable } from '@nestjs/common';

@Injectable()
export class EventsService {
    findAll(): any[] {
        return [
            {
                id: 1,
                name: 'Angular.DE Intensiv Schulung',

            },
            {
                id: 2,
                name: 'Angular.DE Intensiv Schulung 2',

            },
            {
                id: 3,
                name: 'Angular.DE Intensiv Schulung 3',

            },
        ];
    }
}
