class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('Square footage must be a number');
    }
    this._sqft = sqft;

    if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }
}

export default Building;
