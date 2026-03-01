#Run: python smoketest.py to see it work

import openmm as mm
from openmm import unit

# Minimal 2-particle system with a harmonic bond, integrated with Langevin (stochastic dynamics)
system = mm.System()
mass = 39.948 * unit.amu  # arbitrary (argon-ish)
system.addParticle(mass)
system.addParticle(mass)

# Harmonic bond between particle 0 and 1
bond = mm.HarmonicBondForce()
bond.addBond(0, 1, 0.3 * unit.nanometer, 1000 * unit.kilojoule_per_mole / unit.nanometer**2)
system.addForce(bond)

# Integrator (Langevin = Brownian-ish with friction + noise)
integrator = mm.LangevinIntegrator(
    300 * unit.kelvin,
    1.0 / unit.picosecond,
    0.001 * unit.picoseconds
)

# Use Reference platform to guarantee it runs everywhere (slow but bulletproof)
platform = mm.Platform.getPlatformByName("Reference")

context = mm.Context(system, integrator, platform)

# Initial positions
positions = [
    mm.Vec3(0, 0, 0),
    mm.Vec3(0.35, 0, 0),  # slightly stretched vs 0.3nm equilibrium
] * unit.nanometer
context.setPositions(positions)

# Step a little
integrator.step(2000)

state = context.getState(getPositions=True, getEnergy=True)
pos = state.getPositions()
E = state.getPotentialEnergy()

print("Completed OpenMM smoke test.")
print("Potential energy:", E)
print("Final positions (nm):", [(p.x/unit.nanometer, p.y/unit.nanometer, p.z/unit.nanometer) for p in pos])