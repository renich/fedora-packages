Name:           non
Version:        v1.1.0
Release:        1%{?dist}
Summary:        A professional audio production suite.

License:        GPLv2
URL:            http://non.tuxfamily.org/
Source0:        %{name}-%{version}.tar.xz

Requires:       non-things-daw%{?_isa}
Requires:       non-things-mixer%{?_isa}
Requires:       non-things-sequencer%{?_isa}

%description
The Non Things is a powerful, reliable and fast modular Audio Production and
Post Production system, released under the GNU General Public License (GPL). It
utilizes the JACK Audio Connection Kit for inter-application audio I/O and the
FLTK GUI toolkit for a fast and lightweight user interface.

%package %{name}-daw
Summary:        The Non DAW

BuildRequires:  fltk-fluid%{?_isa} >= 1.1.7
BuildRequires:  jack-audio-connection-kit-devel%{?_isa} >= 0.103.0
BuildRequires:  liblo-devel%{?_isa} >= 0.26
BuildRequires:  libsigc++20-devel%{?_isa}
BuildRequires:  libsndfile-devel%{?_isa} >= 0.18.0

%description %{name}-daw
The Non DAW is a powerful, reliable and fast modular Digital Audio Workstation
system, released under the GNU General Public License (GPL). It utilizes the
JACK Audio Connection Kit for inter-application audio I/O and the FLTK GUI
toolkit for a fast and lightweight user interface.

%package %{name}-mixer
Summary:        The Non Mixer

BuildRequires:  fltk-fluid%{?_isa} >= 1.1.7
BuildRequires:  jack-audio-connection-kit-devel%{?_isa} >= 0.103.0
BuildRequires:  liblrdf%{?_isa} >= 0.1.0
BuildRequires:  liblo-devel%{?_isa} >= 0.26
BuildRequires:  libsigc++20-devel%{?_isa}

%description %{name}-mixer

The Non Mixer is a powerful, reliable and fast modular Digital Audio Mixer,
released under the GNU General Public License (GPL). It utilizes the JACK Audio
Connection Kit for inter-application audio I/O and the FLTK GUI toolkit for a
fast and lightweight user interface.

%package %{name}-sequencer
Summary:        The Non Sequencer

BuildRequires:  fltk-fluid%{?_isa} >= 1.1.7
BuildRequires:  jack-audio-connection-kit-devel%{?_isa} >= 0.103.0
BuildRequires:  libsigc++20-devel%{?_isa}

%description %{name}-sequencer
The Non Sequencer is a powerful real-time, pattern-based MIDI sequencer for
Linux--released under the GPL. Filling the void left by countless DAWs,
piano-roll editors, and other purely performance based solutions, it is a
compositional tool--one that transforms MIDI music-making on Linux from a
complex nightmare into a pleasurable, efficient, and streamlined process.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc


%changelog
