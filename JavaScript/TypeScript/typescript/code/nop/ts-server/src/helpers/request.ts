export interface Request {
    protocol: string;
    method: string;
    url: string;
    headers: Map<string, string>;
    body: string;
}


export const parseRequest = (s: string): Request => {
    const [firstLine, rest] = divideStringOn(s, '\r\n');
    const [method, url, protocol] = firstLine.split(' ', 3);
    const [headers, body] = divideStringOn(rest, '\r\n\r\n');
    const parsedHeaders = headers.split('\r\n').reduce((map, header) => {
        const [key, value] = divideStringOn(header, ': ');
        return map.set(key, value);
    }, new Map());
    return { protocol, method, url, headers: parsedHeaders, body };
}

export const divideStringOn = (s: string, search: string) => {
    const index = s.indexOf(search);
    const first = s.slice(0, index);
    const rest = s.slice(index + search.length);
    return [first, rest];
}
