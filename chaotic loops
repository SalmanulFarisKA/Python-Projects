static final int NUM_LINES = 10;

float a = 10;
float b = 0.4;
float c = 10;
float d = 0.1;
float i = 2;
float g = 0;

float t;

void setup(){
  background(20);
  size(1080, 1080);
}

void draw() {
  background(#090421);
  strokeWeight(5);
  
  translate(width/2, height/2);
  
  for (int i=0; i < NUM_LINES; i++){
    
    if(i%10 == 0){
      stroke(#590d22);
    }
    else if(i%10 == 1){
      stroke(#800f2f);
    }
    else if(i%10 == 2){
      stroke(#a4133c);
    }
    else if(i%10 == 3){
      stroke(#c9184a);
    }
    else if(i%10 == 4){
      stroke(#ff4d6d);
    }
    else if(i%10 == 5){
      stroke(#ff758f);
    }
    else if(i%10 == 6){
      stroke(#ff8fa3);
    }
    else if(i%10 == 7){
      stroke(#ffb3c1);
    }
    else if(i%10 == 8){
      stroke(#ffccd5);
    }
    else if(i%10 == 9){
      stroke(#fff0f3);
    }
    
  line(x1(t + i), y1(t + i), x2(t + i), y2(t + i));
  }
  t += 0.5;
  
  scale(4);
  //saveFrame("vintOutput2/vintage_####.png");
}

float x1(float t){
  return ((sin(a*((t-i)-g))/b)+c)*cos((t-i)-sin((sin(2*(t-i))*(t-i))));
}

float y1(float t){
  return ((sin(a*((t-i)-g))/b)+c)*sin((t-i)+sin((sin(2*(t-i))*(t-i))));
}

float x2(float t){
  return ((sin(a*(t-g))/b)+c)*cos(t-d-sin((cos(4*t))*t));
}

float y2(float t){
  return ((sin(a*(t-g))/b)+c)*sin(t-d+sin((cos(4*t))*t));
}
