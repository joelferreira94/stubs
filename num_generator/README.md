# UUID Generator
======

This is a random UUID generator using Python Flask. 
The native app exposes a POST endpoint on port 5001.

To build the image:
```docker build -t generator .```

To run the contanier:
```docker run -it -p 5000:5001 --name gen generator```

