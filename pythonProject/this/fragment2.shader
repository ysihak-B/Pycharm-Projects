#version 330 core
in vec3 newColor;
out vec4 color;

void main()
{
//     color = vec4(1,.5,0, 1.0);
    color = vec4(newColor, 1.0);
}