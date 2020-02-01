=============
Pyxel Physics
=============

A simple physics engine based on Pyxel and Pymunk. The physics API replicates Pyxel's standard API when possible, and adds a few extra options and integrations with Pymunk.

Installation
============

Just ``pip install pyxel-physics --user`` and you are good to go. Advanced users and contributors might prefer to use the git version ``pip install git+http://github.com/fabiommendes/pyxel-physics --user`` or download the repository and install the local development branch using Flit (``flit install -su``

Usage
=====

Most functions have similar names and behaviours as the corresponding functions in Pyxel API.

Creating objects
----------------


Tutorial
========

Let us create a Pong look-alike with more advanced Physics to show off the library. We start importing the Physics module

.. code-block:: python

    import pyxel.phys as phys
    
    WIDTH = 120
    HEIGHT = 80
    
We can create geometric figures by calling the corresponding functions in the ``phys`` module. Just like Pyxel, those functions take a color and some geometric quantities as arguments, but they can also support many physical parameters such as mass, moment of inertial, velocities, etc. We must also remember that physical objects are created into a special "stage" instance and only interact with other objects within the same stage. You can create the stage explicitly, but if you don't, the engine creates a default instance for you.

We can create a paddle as a irrotational rectangle:

.. code-block:: python

    p1 = phys.rect(100, 212)
    p2 = phys.rect(100, 212)

Since ``p1`` and ``p2`` have no mass or moment of inertia, the engine assigns an infinite value to those two quantities. An infinite mass is interpreted as an object that do not respond to forces (since it would require an infinite force to make an effect), but may move and even collide with regular dynamic objects. If a velocity is defined (even if equal to zero) we call those objects "kinematic", which in physics means that we can describe their movement but do not want to talk about the forces that cause it. "Dynamic" objects have their movement influenced by forces (including gravity and collisions) and "static" objects are a special kind of kinematic objects that do not move at all. Pymunk, and physics textbooks for that matter, make a distinction between those three situations, so it is good to keep this nomenclature in mind.  
