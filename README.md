# Face detection for an art installation

## About
A script that projects a pseudo-desktop image to a screen to soduce an observer of an instalation to come closer and look at the contents of the screen. At the same time, a face detection algorithm is being ran in the background with a proximity threshold on detecting a face. When an observer is near enough, pseudo-desktop image on the screen is changed with a webcam stream of the observer and his face tracked on the screen.

Face detection is implemented via built-it Haar Feature-based Cascade Classifier (CV2)

## Input
- webcam stream

## Output
- A) background image that communicates with the visitor (a picture of pseudo desktop of a PC with an intriguing icon)
- B) a live stream of a webcam with a face tracking ractangle.

