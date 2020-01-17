module.exports = {
    verbose: true,
    roots: [
        '<rootDir>/src',
        '<rootDir>/__test__'
    ],
    transform: {
        '^.+\\.ts?$': 'ts-jest'
    },
    testRegex: '(/__test__/.*|(\\.|/)(test|spec))\\.ts?$',
    moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],
    testEnvironment: "node",
    globals: {
        "ts-jest": {
            tsConfig: 'tsconfig.json'
        }
    }
};

// module.exports = {
//     transform: {
//         '^.+\\.ts?$': 'ts-jest'
//     },
//     testEnvironment: 'node',
//     testRegex: '/tests/.*\\.(test|spec)?\\.(ts|tsx|js)$',
//     moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node']
// };