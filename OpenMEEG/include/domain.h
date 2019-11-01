/*
Project Name : OpenMEEG

© INRIA and ENPC (contributors: Geoffray ADDE, Maureen CLERC, Alexandre 
GRAMFORT, Renaud KERIVEN, Jan KYBIC, Perrine LANDREAU, Théodore PAPADOPOULO,
Emmanuel OLIVI
Maureen.Clerc.AT.inria.fr, keriven.AT.certis.enpc.fr,
kybic.AT.fel.cvut.cz, papadop.AT.inria.fr)

The OpenMEEG software is a C++ package for solving the forward/inverse
problems of electroencephalography and magnetoencephalography.

This software is governed by the CeCILL-B license under French law and
abiding by the rules of distribution of free software.  You can  use,
modify and/ or redistribute the software under the terms of the CeCILL-B
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info".

As a counterpart to the access to the source code and  rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty  and the software's authors,  the holders of the
economic rights,  and the successive licensors  have only  limited
liability.

In this respect, the user's attention is drawn to the risks associated
with loading,  using,  modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean  that it is complicated to manipulate,  and  that  also
therefore means  that it is reserved for developers  and  experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or
data to be ensured and,  more generally, to use and operate it in the
same conditions as regards security.

The fact that you are presently reading this means that you have had
knowledge of the CeCILL-B license and that you accept its terms.
*/

#pragma once

/// \file
/// \brief file containing the definition of a Domain.
/// A domain is the association of a name and a vector of pairs.
/// The first element of each pair corresponds to an interface.
/// The second element of each pair states whether the domain is contains in the
/// inside or the ouside of the volume bounded by the interface.

#include <string>
#include <interface.h>

namespace OpenMEEG {

    /// \brief a HalfSpace is a pair of Interface and boolean 
    /// A simple domain (HalfSpace) is given by an interface (of type Interface) identifying a closed surface and a side information.
    /// The closed surface split the space into two components. The side depicts which of these two components is the simple domain.

    class HalfSpace: private std::pair<Interface,bool> {

        typedef std::pair<Interface,bool> base;

    public:

         HalfSpace() { }
         HalfSpace(Interface& interf,const bool ins): base(interf,ins) { }
        ~HalfSpace() { }

              Interface& interface()       { return this->first;  }
        const Interface& interface() const { return this->first;  }

        bool inside() const { return this->second; }
    };

    /// \brief a Domain is a vector of HalfSpace
    /// A Domain is the intersection of simple domains (of type HalfSpace).
    /// In addition the domain is named and has a conductivity.

    class OPENMEEG_EXPORT Domain {
    public:

        typedef std::vector<HalfSpace> Boundaries;

         Domain() { }
        ~Domain() { }

        /// Boundaries of the domain.

              Boundaries& boundaries()       { return bounds; }
        const Boundaries& boundaries() const { return bounds; }

        /// The name of the domain.

              std::string& name()       { return domain_name; }
        const std::string& name() const { return domain_name; }
        
        /// The conductivity of the domain.

              double& conductivity()       { return cond; }
        const double& conductivity() const { return cond; }

        /// Print information about the domain.
        /// \param outermost specifies if the domain is the outer domain
        /// (the geometry knows this information).

        void info(const bool outermost=false) const;

        bool contains(const Vect3& point) const; ///< Does this point belongs to the domain ?

        /// \return 1 if the mesh is oriented towards the inside of the domain.
        ///        -1 if the mesh is oriented towards the outsde of the domain.
        ///         0 otherwise (the mesh is not part of the domain boundary).

        int mesh_orientation(const Mesh& m) const { 
            for (const auto& boundary : boundaries())
                for (const auto& interface : boundary.interface())
                    if (&interface.mesh()==&m)
                        return (boundary.inside()) ? interface.orientation() : -interface.orientation();
            return 0;
        }

    private:

        Boundaries  bounds;             ///< Interfaces (with side) delimiting the domain.
        std::string domain_name = "";   ///< Name of the domain.
        double      cond        = -1.0; ///< Conductivity of the domain.
    };

    /// A vector of Domain is called Domains

    typedef std::vector<Domain> Domains;
}
