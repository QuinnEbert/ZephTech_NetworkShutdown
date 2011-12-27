Quinn Ebert's "ZephTech Network Shutdown Server"
First published on Christmas Day 2011 in the United States
by Quinn Ebert -- on the web at http://quinnebert.net/

FIRST THINGS FIRST -- IMPORTANT LEGAL NOTICE -- REGARDING COPYRIGHTS:
  I"ve tried to do my due diligence here, but, I think it's possible I have
  either missed attributing some code here somewhere, and even, it is quite
  possible that I've re-used code here that is explicitly disallowed to be
  included in open-sourced works.  As a result, and with the assertion on my
  part that I have tried to take the effort to re-write as much of the suspect
  code as I can on my own, I wish to offer an up-front apology to anybody whose
  work I may violate here, and if I have caused any other code author any sort
  of a problem, I offer my up-front promise I will work with you to rectify the
  situation with this codebase to meet your needs upon your notification that I
  may have violated your copyright privileges to any of your works that you can
  offer evidence and validation of how I am in violation here.

  The above having been said, as time goes forward, a lot of the code will be
  re-written.  It is the right thing to do to ensure it is in fact my own code
  in its entirety.

ONE MORE LEGAL NOTICE -- YOU MIGHT LOSE WORK:
  This software provides a mechanism to remotely power off your computer, but,
  this mechanism tries to "force" the shutdown (albeit with some measure of
  grace).  If you have applications open with unsaved work, especially on Linux
  or Windows, you will almost certainly lose the unsaved work.  Mac OS X Lion's
  auto-restore feature might help us avoid this, but don't count on it, I won't
  really test that vigorously before I release this.  Again, you have been told
  about this up front, save your work before shutting down the system with this
  utility.  I cannot be held responsible for lost data and productivity caused
  by this software!

OK -- WHAT IS THIS?
  Many of us geeks find ourselves living (read as "sleeping") in the same room
  as our desktop systems.  When it comes time to sleep, we're tired, we've done
  more than our fair share.  But, darn, we just laid down, and without fail, we
  forgot to turn that machine off. Good grief, I have this mobile phone next to
  me, if only I could use it to turn that blasted machine off!  Well, fret no
  more, I've got your answer here!

  ZephTech Network Shutdown Server provides a theme-able mini web interface you
  can call up on your mobile phone (or pad/tablet) browser to shut down your
  pesky desktop computer!  Just navigate the options it presents you (you will
  access it using the web server on port  on your machine's local IP address)
  and tell it to shut down.

WHAT ARE THE SYSTEM REQUIREMENTS HERE?
  This is written in Python, tested on 32-bit Windows 7, as well as on Mac OS X
  "Lion" and 64-bit Debian 6.
