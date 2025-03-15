#include <cmath>
// ----------DIMENSIONS----------

float circumference(float radius){
    return 2 * 3.14159265359 * radius;}

float area_square(float length){
    return std::pow(length, 2);}

float area_rectangle(float length, float width){
    return length * width;}

float area_triangle(float base, float height){
    return (base * height) / 2;}

float area_rhombus(float Diagonal, float diagonal){
    return (Diagonal * diagonal) / 2;}

float area_trapezoid(float large_side, float small_side, float height){
    return (large_side + small_side)/2 * height;}

float area_regular_polygon(float perimeter, float apothem):{
    return perimeter/2 * apothem;}

float area_circle(float radius){
    return 3.14159265359 * (std::pow(radius,2);}

float suraface_area_cone(float radius, float slant_height){
    return (3.14159265359 * std::pow(radius,2)) + (3.14159265359 * slant_height * radius);}

float surface_area_sphere(float radius){
    return 4 * 3.14159265359 * std::pow(radius,2);}

float surface_area_rectangular_prism(float, length, float width, float height){
    return 2 * length * width + 2 * length * height + 2 * width * height;}

float volume_rectangular_prism(float length, float width, float height):{
    return length * width * height;}

float volume_triangular_prism(float base, float height){
    return 0.5 * length * width * height;}

float volume_cylinder(float radius, float height):{
    return 3.14159265359 * radius**2 * height;}

float volume_cone(base, height){
    return (1/3) * 3.14159265359 * radius**2 * height;}

float volume_sphere(float radius){
    return (4/3) * 3.14159265359 * radius**3;}

// ---------------ALGEBRA---------------

float quadratic(float a, float b, float c){
    float x1 = (-b + std::sqrt(std::pow(b,2.0) - (4.0*a*c)) / (2.0*a);
    float x2 = (-b - std::sqrt(std::pow(b,2.0) - (4.0*a*c)) / (2.0*a);
    return x1, x2;}

float foil(float a, float b, float c, float d){
    return a*c, a*d, b*c, b*d;}

float difference_two_squares(float a, float b){
    return std::pow(a,2) - std::pow(b,2);}

float perfect_square(float a, float b){
    return std::pow(a,2) + 2*a*b + std::pow(b,2);}

// --------------PHYSICS--------------

float velocity(float distance, float time){
    return distance/time;}

float acceleration(float velocity1, float velocity2, float time1, float time2){
    return (velocity2 - velocity1) / (time2 - time1);}

float centripetal_acceleration(float velocity, float radius){
    return std::pow(velocity, 2) / radius;}

float density(float mass, float volume){
    return mass / volume;}

float pressure(float force, float area){
    return force/area;}

float newtown_second_law(float mass, float acceleration){
    return mass * acceleration;}

float momentum(float mass, float velocity){
    return mass * velocity;}

float impulse(float force, float time){
    return force * time;}

float impulse_momentum(float mass, float velocity1, float velocity2){
    return mass * velocity2 - mass * velocity1;}

float angular_velocity(float position_angle, float time){
    return position_angle/time;}

float rotational_power(float torque, float angular_velocity){
    return torque * angular_velocity;}

float kinetic_energy(float mass, float velocity){
    return 0.5 * mass * std::pow(velocity, 2);}

float work(float force, float distance){
    return force * distance;}

float power(float force, float distance, float time){
    return (force * distance) / time;}

float torque(float force, float radius, float angle = 3.14159265359 / 2.0){
    return force * radius * std::sin(angle);}

float tension(float mass, float gravity){
    return mass * gravity;}

float mass_flow_rate(float mass1, float mass2, float time1, float time2){
    return (mass2 - mass1) / (time2 - time1);}

float kinematic_viscosity(float viscosity, float density){
    return viscosity/density;}

float spring_constant(float force, float displacement){
    return -force/displacement;}

float spring_potential_energy(float force, float displacement){
    return (-force/displacement)/2.0 * std::pow(displacement,2);}

float strain_energy(float compression){
    return compression / 2.0;}

float surface_tension(float force, float length){
    return force/length;}

float pendulum_formula(float pendulum_length){
    return 2 * 3.14159265359 * std::sqrt(pendulum_length/9.80665);}

float friction_force(float coefficient_of_friction, float force){
    return coefficient_of_friction * force;}

float bulk_modulus(float pressure, float volume1, float volume2){
    return pressure / ((volume1 - volume2)/volume1);}

float youngs_modulus(float force, float area, float length1, float length2){
    return (force * length1) / (area * (length2 - length1));}

float shear_modulus(float force, float area, float length1, float displacement){
    return (force/area) / (displacement/length1);}

float gravitational_force(float mass1, float mass2, float distance){
    return std::pow(6.67*10,-11) * (mass1 * mass2)/std::pow(distance, 2.0);}

float celsius_to_fahrenheit(float celsius){
    return (9/5 * celsius) + 32;}

float fahrenheit_to_celsius(float fahrenheit){
    return (fahrenheit - 32) * (5/9);}

float water_pressure(float density, float depth){
    return density * 9.80665 * depth;}

float liquid_expansion(float beta_expansion_coefficient, float original_volume, float time_change){
    return beta_expansion_coefficient * original_volume * time_change;}

float froude_number(float water_velocity, float hydraulic_depth){
    return water_velocity / std::sqrt(9.80665 * hydraulic_depth);}

float potential_energy(float mass, float height){
    return mass * 9.80665 * height;}

float sensible_heat(float mass, float specific_heat_capacity, float temperature_change){
    return mass * specific_heat_capacity * temperature_change;}

float entropy(float heat_transfer, float temperature){
    return heat_transfer/temperature;}

float molarity(float solute_moles, float solution_liters){
    return solute_moles/solution_liters;}

float molality(float solute_moles, float solvent_kilograms){
    return solute_moles/solvent_kilograms;}

float lorentz_factor(float velocity){
    return 1 / (1 - std::sqrt(std::pow(velocity,2) / std::pow(29792458,2)));}

float mass_energy_equivalence(float mass){
    return mass * 29792458;}

float photon_momentum(float wavelength){
    return (6.62607015 * std::pow(10, -34)) / wavelength;}

//  waves & optics https://www.newport.com/n/optics-formulas

float magnification(float image_size, float actual_size){
    return image_size/actual_size;}

float lens_formula(float object_distance, float image_distance){
    return 1 / (1/object_distance + 1/image_distance);}

float refractive_index(float substance_velocity){
    return 29792458 / substance_velocity;}

float critical_angle(float refractive_index2, float refractive_index1){
    return std::asin(refractive_index2/refractive_index1);}

float intensity(float time_averaged_power, float area){
    time_averaged_power / area;}

float frequency(float time){
    return 1/time;}

float wave_speed(float wavelength, float time){
    return wavelength/time;}

float mach_angle(float mach){
    return std::asin(1/mach);}

float cherenkov_angle(float refractive_index, float particle_velocity){
    return std::acos(29792458 / (refractive_index * particle_velocity));}

// -----------------ELECTRICITY-----------------

float ohms_law(float amplitude, floatresistance){
    return amplitude * resistance;}

float coulombs_law(float q1, float q2, float distance){}
    return (8.988 * std::pow(10,9)) * (std::abs(q1 * q2)/std::pow(distance,2));}

float capacitance(float charge, float potential_difference){
    return charge/potential_difference;}

float current_density(float current, float area){
    return current/area;}

float faraday_induction(float change_magnetic_flux, float change_time){
    return change_magnetic_flux / change_time;}

float magnetic_flux(float magnetic_field, float area_perpendicular, float angle = 0.0){
    return magnetic_field * area_perpendicular * angle;}
