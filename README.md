# iPy-SNuS
Intel-Accelerated Python Particle Transport Simulation of Nuclear Systems

https://www.researchgate.net/project/OneApi-Python-based-tool-for-Particle-Transport-Simulation-of-Nuclear-Systems


1- First kernel features
  
- Monte Carlo simulation of neutron tracks inside light water.
- The code is parallelized at an event level (performed by the concurrent.futures module).
- Provide high verbosity level.
- Interpolate cross section by using cubic spline method via scipy.interpolate module.


2- How to run

python3 iPy-SNuS.py


3- Simple output

=== iPy-SNuS Monte Carlo neutronique code.

=== Number of cross-section data for isotope 1-H:  307 

=== Number of cross-section data for isotope 16-O:  2503

=== 1-H mass fraction in light water:  0.6666666666666666

=== 16-O mass fraction in light water:  0.3333333333333333

=== Molecular number density of water:(molecules/cm^3) :  3.3324551450773475e+22

=== Atomic number density of Hydrogen in water:(atomes/cm^3) :  2.221636763384898e+22


=== Atomic number density of Oxygen in water:(atomes/cm^3) :  1.110818381692449e+22

=== Molecular number density of water:(molecules/barn-cm) :  0.033324551450773475

=== Atomic number density of Hydrogen in water:(atomes/barn-cm) :  0.02221636763384898

=== Atomic number density of Oxygen in water:(atomes/barn-cm) :  0.01110818381692449

=== Neutron histories:  10

=== Selected incident neutron energy (MeV):  2.0

==========BEGIN OF EVENT# 0 # IN CPU: MainProcess

Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  -1 0.000 0.000 0.000 0.000 0.000 1.000 2000000.000 0.000 None   Transportation
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   0 0.000 0.000 170.822 -0.347 0.744 0.571 663519.953 17.082 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   1 -37.861 81.234 233.231 -0.347 0.744 0.571 657726.641 10.921 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   2 -97.966 210.196 332.308 -0.347 0.744 0.571 605319.399 17.338 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   3 -112.403 241.173 356.106 -0.347 0.744 0.571 547210.455 4.165 16-O   Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   4 -134.022 287.559 391.742 -0.347 0.744 0.571 81336.420 6.236 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   5 -147.596 316.683 414.117 -0.347 0.744 0.571 70580.548 3.916 16-O   Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   6 -165.744 355.622 444.032 -0.347 0.744 0.571 70457.784 5.235 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   7 -166.187 356.572 444.762 -0.347 0.744 0.571 50841.036 0.128 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   8 -186.146 399.396 477.662 -0.347 0.744 0.571 10675.962 5.757 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process

   9 -186.390 399.919 478.064 -0.347 0.744 0.571 2892.770 0.070 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  10 -198.564 426.040 498.132 -0.347 0.744 0.571 1564.206 3.512 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  11 -206.341 442.727 510.952 -0.347 0.744 0.571 1403.099 2.243 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  12 -233.324 500.621 555.429 -0.347 0.744 0.571 644.362 7.783 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  13 -258.052 553.679 596.191 -0.347 0.744 0.571 549.699 7.133 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  14 -259.285 556.325 598.224 -0.347 0.744 0.571 538.303 0.356 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process

  15 -259.566 556.927 598.687 -0.347 0.744 0.571 396.207 0.081 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  16 -265.009 568.606 607.659 -0.347 0.744 0.571 126.373 1.570 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  17 -275.969 592.122 625.726 -0.347 0.744 0.571 46.293 3.161 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  18 -280.986 602.885 633.994 -0.347 0.744 0.571 16.476 1.447 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  19 -298.270 639.971 662.486 -0.347 0.744 0.571 1.654 4.986 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  20 -305.182 654.801 673.879 -0.347 0.744 0.571 0.332 1.994 1-H    Scattering
  
==========END OF EVENT# 0 TOTAL NUMBER OF STEPS:  21

==========BEGIN OF EVENT# 1 # IN CPU: MainProcess

Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  -1 0.000 0.000 0.000 0.000 0.000 1.000 2000000.000 0.000 None   Transportation
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   0 0.000 0.000 293.273 -0.415 0.452 0.790 1253554.766 29.327 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   1 -5.177 5.632 303.125 -0.415 0.452 0.790 333553.581 1.247 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   2 -17.426 18.957 326.434 -0.415 0.452 0.790 231157.927 2.951 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   3 -48.672 52.948 385.895 -0.415 0.452 0.790 72903.377 7.528 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   4 -51.675 56.215 391.611 -0.415 0.452 0.790 51420.748 0.724 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   5 -55.303 60.161 398.514 -0.415 0.452 0.790 33063.913 0.874 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   6 -60.252 65.546 407.933 -0.415 0.452 0.790 19660.979 1.193 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   7 -66.447 72.285 419.721 -0.415 0.452 0.790 19545.356 1.492 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   8 -70.410 76.597 427.264 -0.415 0.452 0.790 3609.717 0.955 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   9 -77.034 83.802 439.868 -0.415 0.452 0.790 1873.384 1.596 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  10 -96.489 104.966 476.891 -0.415 0.452 0.790 268.244 4.687 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  11 -99.280 108.002 482.203 -0.415 0.452 0.790 166.378 0.672 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  12 -104.158 113.309 491.485 -0.415 0.452 0.790 61.029 1.175 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  13 -116.683 126.934 515.321 -0.415 0.452 0.790 19.143 3.018 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  14 -131.323 142.861 543.181 -0.415 0.452 0.790 19.035 3.527 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  15 -133.436 145.159 547.201 -0.415 0.452 0.790 14.491 0.509 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  16 -140.240 152.561 560.150 -0.415 0.452 0.790 12.925 1.639 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  17 -140.601 152.954 560.836 -0.415 0.452 0.790 7.408 0.087 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  18 -149.642 162.789 578.041 -0.415 0.452 0.790 0.256 2.178 1-H    Scattering
  
==========END OF EVENT# 1 TOTAL NUMBER OF STEPS:  19

==========BEGIN OF EVENT# 2 # IN CPU: MainProcess

Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  -1 0.000 0.000 0.000 0.000 0.000 1.000 2000000.000 0.000 None   Transportation
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   0 0.000 0.000 144.999 0.897 0.107 -0.429 1672333.648 14.500 16-O   Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   1 12.421 1.476 139.061 0.897 0.107 -0.429 423940.858 1.385 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   2 91.138 10.831 101.428 0.897 0.107 -0.429 355003.897 8.775 16-O   Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   3 189.992 22.578 54.167 0.897 0.107 -0.429 330285.605 11.020 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   4 331.781 39.428 -13.620 0.897 0.107 -0.429 176509.631 15.806 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   5 335.706 39.894 -15.496 0.897 0.107 -0.429 78629.007 0.438 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   6 351.097 41.723 -22.854 0.897 0.107 -0.429 66135.457 1.716 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   7 377.645 44.878 -35.547 0.897 0.107 -0.429 42916.689 2.960 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   8 378.084 44.930 -35.756 0.897 0.107 -0.429 2124.704 0.049 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

   9 383.153 45.533 -38.180 0.897 0.107 -0.429 1578.493 0.565 1-H    Scattering
   
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  10 386.783 45.964 -39.915 0.897 0.107 -0.429 1384.880 0.405 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  11 399.348 47.457 -45.922 0.897 0.107 -0.429 870.209 1.401 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  12 421.107 50.043 -56.325 0.897 0.107 -0.429 330.103 2.426 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  13 428.573 50.930 -59.894 0.897 0.107 -0.429 118.425 0.832 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  14 454.536 54.016 -72.307 0.897 0.107 -0.429 40.454 2.894 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  15 469.487 55.792 -79.454 0.897 0.107 -0.429 37.943 1.667 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  16 477.141 56.702 -83.114 0.897 0.107 -0.429 10.569 0.853 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  17 490.285 58.264 -89.398 0.897 0.107 -0.429 5.041 1.465 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  18 498.488 59.239 -93.319 0.897 0.107 -0.429 4.857 0.914 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  19 510.500 60.666 -99.062 0.897 0.107 -0.429 1.635 1.339 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  20 522.856 62.135 -104.970 0.897 0.107 -0.429 1.570 1.377 1-H    Scattering
  
Step.ID X(mm)   Y(mm)   Z(mm)   DIR.X   DIR.Y   DIR.Z   K.E(eV) Step.L(cm) Isotope Process 

  21 532.839 63.321 -109.742 0.897 0.107 -0.429 0.830 1.113 1-H    Scattering
  
==========END OF EVENT# 2 TOTAL NUMBER OF STEPS:  22

=== Number of CPU cores:  1

=== Number of histories:  10

=== Neutron kinetic energy (MeV):  2.0

=== First Collision Number: 10

=== Number of interactions: 183

=== Number of capture events: 0

=== Average interaction number:  18.3

=== Capture Fraction (%): 0.0

=== Killed Cutoff (%):  100.0

=== Neutrons killed by Energy Cutoff: 10

=== Total neutron energy  (MeV): 44.415475152033935  MeV

=== Average neutron energy (MeV): 0.24270751449198869

=== Neutron mean life time (s):   2.6864409478294335e-06

=== Average neutron speed (m/s): 3709409.6459378707

=== Average neutron track length (cm):  64.8906192739853

=== Neutron total track length (cm):  648.9061927398529

=== Simulation execution time (seconds):  0.025352
