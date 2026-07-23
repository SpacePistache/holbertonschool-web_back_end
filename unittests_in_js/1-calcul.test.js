const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {

  describe('SUM', function () {

    it('adds integers', function () {
      assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    });

    it('rounds operands before addition', function () {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    });

    it('rounds .5 upward', function () {
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.5), 6);
    });

  });

  describe('SUBTRACT', function () {

    it('subtracts integers', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 4, 2), 2);
    });

    it('rounds operands before subtraction', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 4.6, 2.7), 2);
    });

  });

  describe('DIVIDE', function () {

    it('divides integers', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 6, 3), 2);
    });

    it('rounds operands before division', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('returns Error when divisor rounds to zero', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 2, 0.2), 'Error');
    });

    it('returns Error when divisor is zero', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 2, 0), 'Error');
    });

  });

});
