#
# Conditional build:
%bcond_without	doc		# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	flask-script
Summary:	Scripting support for Flask
Summary(pl.UTF-8):	Wsparcie dla skryptów w Flask-
# Name must match the python module/package name (as in 'import' statement)
Name:		python-%{module}
Version:	2.0.5
Release:	6
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/F/Flask-Script/Flask-Script-%{version}.tar.gz
# Source0-md5:	e5c73d3b7937f5b88942f342f9617029
URL:		http://github.com/smurfix/flask-script
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	rpm-pythonprov
%if %{with python2}
BuildRequires:	python-distribute
BuildRequires:	python-flask
BuildRequires:	python-itsdangerous
BuildRequires:	python-pytest
%endif
%if %{with python3}
BuildRequires:	python3-distribute
BuildRequires:	python3-flask
BuildRequires:	python3-itsdangerous
BuildRequires:	python3-modules
BuildRequires:	python3-pytest
%endif
Requires:	python-modules
Requires:	python-flask
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Flask-Script extension provides support for writing external
scripts in Flask. This includes running a development server, a
customised Python shell, scripts to set up your database, cronjobs,
and other command-line tasks that belong outside the web application
itself.

%description -l pl.UTF-8
Rozszerzenie Flask-Script pozwala na pisanie zewnętrznych skryptów w
Flasku. Co dalej pozawala na uruchamianie serwera rozwojowego,
własnych skryptów w Pythonie, skryptów inicjujących bazę dane,
skryptów cronta i różnych inych zadań z lini poleceń, które nie należą
do samej aplikacji.

%package -n python3-%{module}
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-flask

%description -n python3-%{module}
The Flask-Script extension provides support for writing external
scripts in Flask. This includes running a development server, a
customised Python shell, scripts to set up your database, cronjobs,
and other command-line tasks that belong outside the web application
itself.

%description -n python3-%{module} -l pl.UTF-8
Rozszerzenie Flask-Script pozwala na pisanie zewnętrznych skryptów w
Flasku. Co dalej pozawala na uruchamianie serwera rozwojowego,
własnych skryptów w Pythonie, skryptów inicjujących bazę dane,
skryptów cronta i różnych inych zadań z lini poleceń, które nie należą
do samej aplikacji.


%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n Flask-Script-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif



%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py_sitescriptdir}/flask_script
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/Flask_Script-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py3_sitescriptdir}/flask_script
%{py3_sitescriptdir}/Flask_Script-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
