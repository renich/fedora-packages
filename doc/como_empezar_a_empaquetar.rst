#####################################
Cómo empezar a empaquetar para Fedora
#####################################
---------------------------------------------------
Guía práctica para empezar a empaquetar para Fedora
---------------------------------------------------

:Autor:
    Renich Bon Ciric <renich@woralelandia.com>

:Licencia:
    FDL_ 1.3 o >

:Versión:
    20140501

.. raw:: pdf

    PageBreak oneColumn

.. contents::

.. section-numbering::

.. raw:: pdf

    PageBreak oneColumn


Descripción
===========
En esta guía, te voy a ayudar a explorar como crear tus paquetes para Fedora.

La idea es ayudarte a empezar rápido a empaquetar. Luego, vamos a ir con los detalles de los
`Lineamientos de Empaquetamiento de Fedora`_ y lo relacionado.

Por lo pronto, manos a la obra.

De qué se trata
---------------
Básicamente, lo que vamos a hacer es automatizar la compilación y parchado de alguna pieza de software. Para ésto, debemos estar
muy bien familiarizados con el procedimiento de compilación manual. Por ejemplo:

    * Saber qué dependencias tiene.
    * Saber si es estandard el procedimiento de compilación.
    * Estar en contacto con *upstream* y tenerle al tanto de nuestras intenciones; bugs y mejoras que pudiera tener el paquete.

Una vez teniendo todo ésto, podemos comenzar a empaquetar algo.

Una vez que sabemos los detalles del paquete, debemos generar un archivo *spec* y proceder a la construcción del paquete.

Cualquier cambio que queramos hacer en el paquete; como, por ejemplo, editar un poco el Makefile, debe ser a través de parches. He
aquí una guía para hacerlo: https://fedoraproject.org/wiki/How_to_create_an_RPM_package#.25prep_section:_.25patch_commands


Configuración
=============
Lo primero que hay que leer es el `How to create a GNU hello RPM package`_.

En resumen, nos van a pedir que:

.. code-block:: Bash

    # descarguemos lo necesario
    su -c 'yum install @development-tools fedora-packager'

    # nos hagamos miembros del grupo mock
    su -c 'usermod -aG mock ${USER}'
    newgrp mock

    # generemos nuestro ambiente de empaquetamiento
    rpmdev-setuptree


Construcción
============
Ahora, a lo que nos concierne. Vamos a consturir nuestro primer paquete.

.. code-block:: Bash

    # vallamos al directorio de trabajo
    cd ~/rpmbuild

    # generemos un spec
    cat << 'EOF' > ~/rpmbuild/SPECS/hello.spec
    Name:           hello
    Version:        2.8
    Release:        1%{?dist}
    Summary:        The "Hello World" program from GNU

    License:        GPLv3+
    URL:            http://ftp.gnu.org/gnu/%{name}
    Source0:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

    BuildRequires: gettext

    Requires(post): info
    Requires(preun): info

    %description
    The "Hello World" program, done with all bells and whistles of a proper FOSS
    project, including configuration, build, internationalization, help files, etc.

    %prep
    %autosetup

    %build
    %configure
    make %{?_smp_mflags}

    %install
    %make_install
    %find_lang %{name}
    rm -f %{buildroot}/%{_infodir}/dir

    %post
    /sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

    %preun
    if [ $1 = 0 ] ; then
    /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
    fi

    %files -f %{name}.lang
    %doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
    %{_mandir}/man1/hello.1.gz
    %{_infodir}/%{name}.info.gz
    %{_bindir}/hello

    %changelog
    * Tue Sep 06 2011 The Coon of Ty <Ty@coon.org> 2.8-1
      - Initial version of the package
    EOF

    # obtengamos la fuente
    cd ~/rpmbuild/SOURCES
    spectool -g ~/rpmbuild/SPECS/hello.spec

    # generemos el SRPM
    rpmbuild -bs ~/rpmbuild/SPECS/hello.spec

    # lo compilemos usando mock
    mock --results-dir ~/rpmbuild/results --rebuild SRPMS/hello-2.8-1.fc20.src.rpm

    # lo revisemos
    rpmlint ~/rpmbuild/{SRPMS,SPECS}/hello*

.. note::
    Es muy importante darnos cuenta de que los HowTos en la Wiki de Fedora; como en todos lados, están desactualizados.

    En nuestro caso, podemos confiar en que los `Lineamientos de Empaquetamiento de Fedora`_ están actuales; mas los
    Howtos o ejemplos, no.

    Es importante que consultemos con algún empaquetador experimentado, en el canal de IRC: #fedora-devel @ irc, o en
    la lista de correo fedora-devel.

.. raw:: pdf

    PageBreak oneColumn

Recomendaciones generales
=========================
Aquí pondré algunas de las recomendaciones que, a mi parecer, son pertinentes y útiles.

Scripts
-------
Hay cosas que son tediosas y nos desenfocan. Por ejemplo, estar escribiendo comandos repetitivos una y otra vez.

Por ésto, recomiendo que tengas una carpeta *~/rpmbuild/scripts*; en donde pondrás un script para facilitar tu trabajo.

Tengo un buen ejemplo de ésto en: https://github.com/renich/fedora-packages/blob/hhvm/scripts/build-hhvm

Git
---
Recomiendo que utilices git_ para manejar:
    * tus archivos spec
    * tus parches
    * tus scripts

Básicamente, te sugiero que ignores todo menos:

::

    ~/rpmbuild/SPECS
    ~/rpmbuild/SOURCES/*.patch
    ~/rpmbuild/scripts/

Eso lo logramos con un *.gitignore*:

::

    !SOURCES/*.patch
    BUILD*/
    SRPMS/*
    RPMS/*
    SOURCES/*
    results/*

Hay un ejemplo muy concreto en: https://github.com/renich/fedora-packages/tree/hhvm


.. Links
.. _FDL: http://www.gnu.org/licenses/fdl.txt
.. _Lineamientos de Empaquetamiento de Fedora: https://fedoraproject.org/wiki/Packaging:Guidelines
.. _How to create a GNU hello RPM package: https://fedoraproject.org/wiki/How_to_create_a_GNU_Hello_RPM_package
.. _git: https://git-scm.com/
