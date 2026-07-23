const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  it('returns the sum of two integers', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('rounds the first number down', function () {
    assert.strictEqual(calculateNumber(1.2, 3), 4);
  });

  it('rounds the first number up', function () {
    assert.strictEqual(calculateNumber(1.7, 3), 5);
  });

  it('rounds the first number at .5 upward', function () {
    assert.strictEqual(calculateNumber(1.5, 3), 5);
  });

  it('rounds the second number down', function () {
    assert.strictEqual(calculateNumber(1, 3.2), 4);
  });

  it('rounds the second number up', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('rounds the second number at .5 upward', function () {
    assert.strictEqual(calculateNumber(1, 3.5), 5);
  });

  it('rounds both numbers down', function () {
    assert.strictEqual(calculateNumber(1.2, 3.2), 4);
  });

  it('rounds both numbers up', function () {
    assert.strictEqual(calculateNumber(1.7, 3.7), 6);
  });

  it('rounds both numbers at .5 upward', function () {
    assert.strictEqual(calculateNumber(1.5, 3.5), 6);
  });
});
