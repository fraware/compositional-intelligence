/** Finite illustration of item-level agreement and independent adequacy.
 * No experimental results or claims about model behavior are encoded here.
 */
export const UNIVERSE = Object.freeze([1, 2, 3, 4]);
export const MODES = Object.freeze(['faithful', 'collapsed', 'spurious']);

/** Normalize a finite source/target set, rejecting out-of-domain values. */
function setOf(values) {
  if (!Array.isArray(values) || values.some((n) => !Number.isInteger(n) || !UNIVERSE.includes(n))) {
    throw new TypeError('Expected a subset of {1, 2, 3, 4}.');
  }
  return [...new Set(values)].sort((a, b) => a - b);
}

function checkMode(mode) {
  if (!MODES.includes(mode)) throw new RangeError(`Unknown transport: ${String(mode)}`);
}

const equalSets = (a, b) => a.length === b.length && a.every((n, i) => n === b[i]);
const targetReference = (source) => setOf(source).filter((n) => n % 2 === 0);
const sourceTransform = (source) => setOf([...source, 1]);
const targetTransform = (target) => setOf(target); // Identity: adding odd 1 leaves the even subset unchanged.

function transport0(source, mode) {
  checkMode(mode);
  return mode === 'collapsed' ? [] : targetReference(source);
}

function transport1(transformedSource, mode) {
  checkMode(mode);
  if (mode === 'collapsed') return [];
  const faithful = targetReference(transformedSource);
  return mode === 'spurious' ? setOf([...faithful, 4]) : faithful;
}

/** Compare both well-typed paths and both independently specified reference outputs. */
export function inspectItem(source, mode) {
  checkMode(mode);
  const x = setOf(source);
  const fx = sourceTransform(x);
  const translatedSource = transport0(x, mode);
  const viaSource = transport1(fx, mode); // T1(f(x))
  const viaTarget = targetTransform(translatedSource); // g(T0(x))
  const referenceSource = targetReference(fx);
  const referenceTarget = targetReference(x);
  return {
    x, fx, translatedSource, viaSource, viaTarget,
    agreement: equalSets(viaSource, viaTarget),
    adequate: equalSets(viaSource, referenceSource) && equalSets(translatedSource, referenceTarget),
  };
}

/** Exhaust the full powerset of the four-element source universe (16 items). */
export function evaluateDomain(mode) {
  checkMode(mode);
  let agreement = 0;
  let adequate = 0;
  let jointlyAccepted = 0;
  for (let mask = 0; mask < 1 << UNIVERSE.length; mask += 1) {
    const x = UNIVERSE.filter((_, i) => (mask & (1 << i)) !== 0);
    const outcome = inspectItem(x, mode);
    agreement += Number(outcome.agreement);
    adequate += Number(outcome.adequate);
    jointlyAccepted += Number(outcome.agreement && outcome.adequate);
  }
  return { total: 1 << UNIVERSE.length, agreement, adequate, jointlyAccepted };
}

/** Convert a finite set to a stable, readable label. */
export function formatSet(values) {
  return values.length ? `{${values.join(', ')}}` : '∅';
}

function mountStudy(root) {
  const modeControl = root.querySelector('#transport');
  const memberControls = [...root.querySelectorAll('input[name="member"]')];
  const output = (id, value) => {
    const node = root.querySelector(`#${id}`);
    if (node) node.textContent = value;
  };

  const explanation = (item) => {
    if (item.agreement && item.adequate) {
      return 'These paths agree, and both transports match the independently defined even-subset reference for this input. One passing item does not establish correctness on other inputs.';
    }
    if (item.agreement) {
      return 'The two paths agree, yet at least one transport disagrees with the independent reference. Path agreement alone is insufficient evidence of semantic adequacy.';
    }
    return 'The paths disagree under exact set equality. This item also fails the independent adequacy check. A failed square does not, by itself, identify a unique causal fault.';
  };

  function render() {
    const mode = modeControl.value;
    const source = memberControls.filter((box) => box.checked).map((box) => Number(box.value));
    const result = inspectItem(source, mode);
    const domain = evaluateDomain(mode);
    output('source-x', formatSet(result.x));
    output('source-fx', formatSet(result.fx));
    output('target-t0', formatSet(result.translatedSource));
    output('target-a', formatSet(result.viaSource));
    output('target-b', formatSet(result.viaTarget));
    output('agreement-result', result.agreement ? 'Yes' : 'No');
    output('adequacy-result', result.adequate ? 'Yes' : 'No');
    output('domain-agreement', `${domain.agreement}/${domain.total}`);
    output('domain-adequacy', `${domain.adequate}/${domain.total}`);
    output('domain-joint', `${domain.jointlyAccepted}/${domain.total}`);
    output('interpretation', explanation(result));
  }

  root.addEventListener('change', render);
  render();
}

// Importing this module into Node for reproducible tests performs no DOM operations.
if (typeof document !== 'undefined') {
  const root = document.getElementById('commuting-study');
  if (root) mountStudy(root);
}
