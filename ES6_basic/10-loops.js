export default function appendToEachArrayValue(array, appendString) {
  const idx = 0;
  for (const idx of array) {
    const value = array[idx];
    array[idx] = appendString + value;
  }

  return array;
}
