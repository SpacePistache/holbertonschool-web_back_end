class Car {
  constructor(brand, motor, color) {
	this._brand = brand;
	this.color = color;
	this.motor = motor;
  }

  cloneCar() {
	const ClonedCar = Object.getPrototypeOf(this).constructor;
	return new ClonedCar(this._brand, this._motor, this._color);
  }
}
