class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._color = color;
    this._motor = motor;
  }

  cloneCar() {
    const ClonedCar = Object.getPrototypeOf(this).constructor;
    return new ClonedCar(this._brand, this._motor, this._color);
  }
}
export default Car;
