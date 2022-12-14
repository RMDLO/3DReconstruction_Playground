.. Notes and doc on dense matching

Dense Matching Notes
====================


Backprojection at a given depth
-------------------------------

The backprojection of a pixel :math:`q = (q_x, q_y, 1)^T` at depth :math:`d` in camera coordinates is

.. math::

   X = d K^{-1} q

Backprojection to a plane
-------------------------

The backprojection of a pixel :math:`q = (q_x, q_y, 1)^T` on to the plane :math:`\pi = (v^T, 1)` is

.. math::
   X = \frac{-K^{-1} q}{v^T K^{-1} q}

and has depth

.. math::
   d = \frac{-1}{v^T K^{-1} q}



Plane given point and normal
----------------------------

The plane

.. math::

   \pi = \left( \frac{-n^T}{n^T X}, 1 \right)

Contains the point :math:`X` and has normal :math:`n`


Plane of constant depth
-----------------------

A plane of constant depth :math:`d` is defined by :math:`z = d` in camera coordinates.
So it has de following coordinates

.. math::

   \pi_c = (0, 0, -1 / d, 1)


Plane coordinates conversion
----------------------------

The coordinates of a plane in world and camera coordinates are related by

.. math::

   \pi_w = \begin{pmatrix} R & t \\ 0 & 1 \end{pmatrix} \pi_c


Plane-induced homography
------------------------

Given a plane in camera coordinates :math:`\pi_c = (v^T 1)` the homography from image 1 to image 2 is given by

.. math::

   H = K_2 [R_2 R_1^T + (R_2 R_1^T t_1 - t_2) v^T] K_1^{-1}

We can pre-compute

.. math::

   Q_{12} &= R_2 R_1^T \\
   a_{12} &= R_2 R_1^T t_1 - t_2

and then we have

.. math::

   H = K_2 [Q_{12} + a_{12} v^T] K_1^{-1}


Local, affine approximation of an homography
--------------------------------------------

The homography mapping defined by matrix :math:`H` is

.. math::

   f(x, y) = \begin{pmatrix} u / w \\
                             v / w \end{pmatrix}

where

.. math::
   u &= H_1 (x, y, 1)^T \\
   v &= H_2 (x, y, 1)^T \\
   w &= H_3 (x, y, 1)^T

The differential is then

.. math::

   Df(x, y) = \frac{1}{w^2}
      \begin{pmatrix}
         H_{11} w - H_{31} u  &  H_{12} w - H_{32} u \\
         H_{21} w - H_{31} v  &  H_{22} w - H_{32} v
      \end{pmatrix}

And the linear approximation around :math:`(x_0, y_0)` is

.. math::

   f(x_0 + dx, y_0 + dy) = f(x_0, y_0) + Df(x_0, y_0)(dx, dy)^T


Undistortion
------------

The dense module assumes that images are taken with perspective projection and no radial distortion.  For perspective images, undistorted versions can be generated by taking into account the computed distortion parameters, :math:`k1` and :math:`k2`.

Spherical images (360 panoramas) however can not be unwarped into a single perspective view.  We need to generate multiple perspective views to cover the field of view of a panorama.

This means that the undistortion process will create new views of the reconstruction.  Thus the undistortion process is one where a reconstruction is taken as input and a new reconstruction is produced as output.  The input may contain radially distorted images and panoramas and the output reconstruction will only have undistorted perspective images.

Also, because new views are generated, a new track graph is also generated.

