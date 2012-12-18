"""
.. currentmodule:: pygmin.takestep

Step Taking
===========

The performance of the basin hopping critically depends on the step taking algorithm. 
Pygmin comes with a set of basic takestep routines. For anything non-standard, the user is encouraged
to implement a custom takestep routine.

Basic steptaking
++++++++++++++++

.. autosummary::
   :toctree: generated/

    RandomDisplacement
    UniformDisplacement
    RotationalDisplacement
    
Grouping moves + adaptive steptaking
++++++++++++++++++++++++++++++++++++

.. autosummary::
   :toctree: generated/

    AdaptiveStepsize
    AdaptiveStepsizeTemperature
    GroupSteps
    BlockMoves
    Reseeding

Writing custom steptaking routines
++++++++++++++++++++++++++++++++++
Pygmin makes it very simple to design custom takestep routines. Any takestep class should have
TakestepInterface as a parent class (directly derived from that or a child class of TakestepInterface).

::

    from pygmin.takestep import TakestepInterface
    from pygmin.takestep import buildingblocks as bb
    
    class MyStep(TakestepInterface):
        def takeStep(self, coords, **kwargs):
            # create an rigid body coordinate interface for coordinates array
            ca = CoordsAdapter(nrigid=GMIN.getNRigidBody(), nlattice=6, coords=coords)
            
            # rotate one random rigid body
            select = [np.random.randint(0,nrigid)]
            bb.rotate(1.6, ca.rotRigid, indices = select)

Building blocks to design custom takestep routines

.. autosummary::

    uniform_displace
    rotate
    reduced_coordinates_displace
    

The takestep interface

.. autosummary::

    TakestepInterface
    Takestep
    TakestepSlice


"""


from buildingblocks import *
from generic import *
from group import *
from adaptive import *
from displace import *
from adaptive_step_temperature import *
