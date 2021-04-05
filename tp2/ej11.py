# Conoces Pypi? Es un sitio con gran variedad de librerías que podés instalar libremente a
# través de la herramienta pip. Te permite buscar proyectos según el área de interés. Queremos
# procesar esta lista de categorías como un string para poder saber las subcategorías tiene cada
# una. Copia el contenido del archivo categorias como contenido de una variable string para
# poder obtener información de la cantidad de subcategorías y la lista que incluye cada categoría.
# Nota: no es necesario diferenciar las subcategorías que se encuentren anidadas.

# Ver Ejemplo: De la categoría ‘Communications’ hay 23 subcategorías, y se debe contar con la lista
# que se encuentran dentro de la misma.

import string

texto = """ptive Technologies
Artistic Software
Communications

    BBS
    Chat
        ICQ
        Internet Relay Chat
        Unix Talk 
    Conferencing
    Email
        Address Book
        Email Clients (MUA)
        Filters
        Mail Transport Agents
        Mailing List Servers
        Post-Office
            IMAP
            POP3 
    FIDO
    Fax
    File Sharing
        Gnutella 
    Ham Radio
    Internet Phone
    Telephony
    Usenet News 

Database

    Database Engines/Servers
    Front-Ends 

Desktop Environment

    File Managers
    GNUstep
    Gnome
    K Desktop Environment (KDE)
    Screen Savers
    Window Managers
        Blackbox
        Fluxbox
        XFCE 

Documentation

    Sphinx 

Education

    Computer Aided Instruction (CAI)
    Testing 

Games/Entertainment

    Arcade
    Board Games
    First Person Shooters
    Fortune Cookies
    Multi-User Dungeons (MUD)
    Puzzle Games
    Real Time Strategy
    Role-Playing
    Side-Scrolling/Arcade Games
    Simulation
    Turn Based Strategy 

Home Automation
Internet

    File Transfer Protocol (FTP)
    Finger
    Log Analysis
    Name Service (DNS)
    Proxy Servers
    WAP
    WWW/HTTP
        Browsers
        Dynamic Content
            CGI Tools/Libraries
            Content Management System
            Message Boards
            News/Diary
            Page Counters
            Wiki 
        HTTP Servers
        Indexing/Search
        Session
        Site Management
            Link Checking 
        WSGI
            Application
            Middleware
            Server 
    XMPP
    Z39.50 

Multimedia

    Graphics
        3D Modeling
        3D Rendering
        Capture
            Digital Camera
            Scanners
            Screen Capture 
        Editors
            Raster-Based
            Vector-Based 
        Graphics Conversion
        Presentation
        Viewers 
    Sound/Audio
        Analysis
        CD Audio
            CD Playing
            CD Ripping
            CD Writing 
        Capture/Recording
        Conversion
        Editors
        MIDI
        Mixers
        Players
            MP3 
        Sound Synthesis
        Speech 
    Video
        Capture
        Conversion
        Display
        Non-Linear Editor 

Office/Business

    Financial
        Accounting
        Investment
        Point-Of-Sale
        Spreadsheet 
    Groupware
    News/Diary
    Office Suites
    Scheduling 

Other/Nonlisted Topic
Printing
Religion
Scientific/Engineering

    Artificial Intelligence
    Artificial Life
    Astronomy
    Atmospheric Science
    Bio-Informatics
    Chemistry
    Electronic Design Automation (EDA)
    GIS
    Human Machine Interfaces
    Hydrology
    Image Processing
    Image Recognition
    Information Analysis
    Interface Engine/Protocol Translator
    Mathematics
    Medical Science Apps.
    Physics
    Visualization 

Security

    Cryptography 

Sociology

    Genealogy
    History 

Software Development

    Assemblers
    Bug Tracking
    Build Tools
    Code Generators
    Compilers
    Debuggers
    Disassemblers
    Documentation
    Embedded Systems
    Internationalization
    Interpreters
    Libraries
        Application Frameworks
        Java Libraries
        PHP Classes
        Perl Modules
        Pike Modules
        Python Modules
        Ruby Modules
        Tcl Extensions
        pygame 
    Localization
    Object Brokering
        CORBA 
    Pre-processors
    Quality Assurance
    Testing
        Acceptance
        BDD
        Mocking
        Traffic Generation
        Unit 
    User Interfaces
    Version Control
        Bazaar
        CVS
        Git
        Mercurial
        RCS
        SCCS 
    Widget Sets 

System

    Archiving
        Backup
        Compression
        Mirroring
        Packaging 
    Benchmark
    Boot
        Init 
    Clustering
    Console Fonts
    Distributed Computing
    Emulators
    Filesystems
    Hardware
        Hardware Drivers
        Mainframes
        Symmetric Multi-processing
        Universal Serial Bus (USB) 
    Installation/Setup
    Logging
    Monitoring
    Networking
        Firewalls
        Monitoring
            Hardware Watchdog 
        Time Synchronization 
    Operating System
    Operating System Kernels
        BSD
        GNU Hurd
        Linux 
    Power (UPS)
    Recovery Tools
    Shells
    Software Distribution
    System Shells
    Systems Administration
        Authentication/Directory
            LDAP
            NIS 

Terminals

    Serial
    Telnet
    Terminal Emulators/X Terminals 

Text Editors

    Documentation
    Emacs
    Integrated Development Environments (IDE)
    Text Processing
    Word Processors 

Text Processing

    Filters
    Fonts
    General
    Indexing
    Linguistic
    Markup
        HTML
        LaTeX
        Markdown
        SGML
        VRML
        XML
        reStructuredText 

Utilities
"""

lineas2 = texto.split("\n")
""" lineas = lineas.copy()

tabs_linea_max = 0
tabs_linea = 0
len_lineas_antes = len(lineas)
aux = 0
for linea in lineas:
    tabs_linea = 0
    if len(linea) <= 1:
        print("No es printable:")
        aux+=1
        lineas.remove(linea)
    else:
        if linea.startswith(" "):
            tabs_linea = linea.count("    ")
            if tabs_linea > tabs_linea_max:
                tabs_linea_max = tabs_linea
        print(f"Nivel de categoria: {tabs_linea}. Linea: {linea}\n")

print(f"Len de lineas: {len(lineas)} y antes era: {len_lineas_antes}, aux: {aux}, cant tabs max: {tabs_linea_max}\n\n") """

############## Version B como en la practica simple:
filtros = {}
for cada_linea in lineas2:   
    if not len(cada_linea) == 0:
        if not cada_linea.split(' ')[0] == '':
            filtros[cada_linea] = []
            filtro_actual = cada_linea
        else:
             filtros[filtro_actual].append(cada_linea.strip())

i = 1
for cada_filtro in filtros.keys():
    print(f"\n#  Categoria: {cada_filtro}\n{i:<2d} Cantidad elementos: {len(filtros.get(cada_filtro))}")
    for n in filtros.get(cada_filtro):
        print(f"     {n:<10}")
    i+=1
