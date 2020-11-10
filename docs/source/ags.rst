Athabasca well logs
====================

.. autofunction:: petrodc.ags.get_las

.. autofunction:: petrodc.ags.plot_log

Example
-------

.. code-block:: python

    >>> import petrodc.ags as ags
    >>> las_files = ags.get_las(2)      # fetch the first 2 well logs from the Special Report 006 Athabasca Oil Sands Data
    >>> my_las = list(las_files.values())[1]        # get its respective df from dict
    >>> ags.plot_log(my_las).show()     # plotting logs

|well-log|

.. |well-log| image:: /figures/well-log.png
                    :scale: 40%

Web Application
---------------

There is also the web-app based on petrodc:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/1oj_e-XhirQ?start=36" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
