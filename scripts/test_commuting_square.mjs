/** Exact, dependency-free tests for the published finite study. */
import assert from 'node:assert/strict';
import test from 'node:test';
import { evaluateDomain, formatSet, inspectItem, MODES, UNIVERSE } from '../docs/studies/commuting-square.mjs';

const cases = [
  { mode: 'faithful', agreement: 16, adequate: 16, jointlyAccepted: 16 },
  { mode: 'collapsed', agreement: 16, adequate: 4, jointlyAccepted: 4 },
  { mode: 'spurious', agreement: 8, adequate: 8, jointlyAccepted: 8 },
];

for (const expected of cases) {
  test(`exhaustive counts for ${expected.mode}`, () => {
    assert.deepEqual(evaluateDomain(expected.mode), { total: 16, agreement: expected.agreement,
      adequate: expected.adequate, jointlyAccepted: expected.jointlyAccepted });
  });
}

test('the displayed default input has two matching, adequate outputs', () => {
  const item = inspectItem([2, 3], 'faithful');
  assert.deepEqual(item.x, [2, 3]);
  assert.deepEqual(item.fx, [1, 2, 3]);
  assert.deepEqual(item.translatedSource, [2]);
  assert.deepEqual(item.viaSource, [2]);
  assert.deepEqual(item.viaTarget, [2]);
  assert.equal(item.agreement, true);
  assert.equal(item.adequate, true);
});

test('collapsed transport commutes but loses source distinctions', () => {
  const item = inspectItem([2, 3], 'collapsed');
  assert.equal(item.agreement, true);
  assert.equal(item.adequate, false);
  assert.deepEqual(item.viaSource, []);
  assert.deepEqual(item.viaTarget, []);
});

test('spurious target output produces disagreement, except where hidden by the input', () => {
  assert.equal(inspectItem([2, 3], 'spurious').agreement, false);
  const masked = inspectItem([2, 4], 'spurious');
  assert.equal(masked.agreement, true);
  assert.equal(masked.adequate, true);
});

test('input validation and stable mathematical labels', () => {
  assert.deepEqual(inspectItem([4, 2, 2], 'faithful').x, [2, 4]);
  assert.throws(() => inspectItem([5], 'faithful'), TypeError);
  assert.throws(() => inspectItem([1], 'unknown'), RangeError);
  assert.deepEqual(MODES, ['faithful', 'collapsed', 'spurious']);
  assert.deepEqual(UNIVERSE, [1, 2, 3, 4]);
  assert.equal(formatSet([]), '∅');
  assert.equal(formatSet([2, 4]), '{2, 4}');
});
