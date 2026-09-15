import { useState } from "react";

/*
 * Assumption made explicit per the spec's ambiguity requirement:
 * if initial > max, the value is CLAMPED to max (not thrown), since
 * a UI counter should stay usable rather than crash on bad input.
 */
function Counter({ max, initial = 0 }) {
  const clampedInitial = Math.min(initial, max);
  const [value, setValue] = useState(clampedInitial);

  return (
    <div>
      <button onClick={() => setValue(v => v - 1)} disabled={value <= 0}>
        -
      </button>
      <span>{value}</span>
      <button onClick={() => setValue(v => v + 1)} disabled={value >= max}>
        +
      </button>
      <button onClick={() => setValue(clampedInitial)}>Reset</button>
    </div>
  );
}

export default Counter;
