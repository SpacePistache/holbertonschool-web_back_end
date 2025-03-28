class Car {
  constructor(brand = undefined, motor = undefined, color = undefined) {
    this._brand = brand;
    this._color = color;
    this._motor = motor;
  }

  cloneCar() {
    const ClonedCar = Object.getPrototypeOf(this).constructor;
    return new ClonedCar();
  }
}
export default Car;
