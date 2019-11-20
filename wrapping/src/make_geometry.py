# Build a geometry with given interfaces and domains.


def make_geometry(interfaces, domains, meshes=None):
    """Make a geometry from dictionary of domains and a list of interfaces


    Parameters
    ----------
    interfaces : list
        The XXX
    domains : dict
        The domains.

    Returns
    -------
    geometry : isinstance of om.Geometry
        The geometry that can be used in OpenMEEG.
    """

    if not isinstance(domains, dict) or len(domains) == 0:
        raise Exception(
            "Wrong argument (should be a non empty dictionary of named domains)")

    # This would be better with a set() but newer swig does not provide the
    # __hash__ method.

    meshes = list()
    geom = Geometry()
    for dname, domain in domains.items():
        domain_interfaces, conductivity = domain

        if not isinstance(domain_interfaces, list) or len(domain_interfaces) == 0:
            raise Exception("wrong description of domain (" +
                            dname + "), should be a non-empty list of interfaces")

        om_domain = Domain(dname)
        om_domain.set_conductivity(conductivity)

        for iname, side in domain_interfaces:
            if iname not in interfaces:
                raise Exception(
                    "Domain " + dname + " contains and unknown interface " + iname + ".")
            oriented_meshes = interfaces[iname]
            if type(oriented_meshes) != list or len(oriented_meshes) == 0:
                raise Exception("Interface definition " + iname +
                                " first argument should be a non-empty list of (mesh,orientation)")
            if side != SimpleDomain.Inside and side != SimpleDomain.Outside:
                raise Exception(
                    "Domain " + dname + ": interface " + iname + " has a wrong side direction (In/Out)")

            om_interface = Interface(iname)
            for mesh, orientation in oriented_meshes:
                if type(mesh) != type(Mesh()):
                    raise Exception(
                        "Wrong description of interface (" + iname + "), first tuple member should a be a mesh")
                if orientation != OrientedMesh.Normal and orientation != OrientedMesh.Opposite:
                    raise Exception(
                        "Wrong description for interface (" + iname + "), second tuple member should a be an orientation")

                print("Mesh:", mesh)
                mesh.info()
                if mesh not in meshes:
                    meshes.append(mesh)
                oriented_mesh = OrientedMesh(mesh, orientation)
                om_interface.oriented_meshes().push_back(oriented_mesh)

            om_domain.boundaries().push_back(SimpleDomain(om_interface, side))
        geom.domains().push_back(om_domain)

    geom.import_meshes(list(meshes))
    geom.finalize()
    return geom
