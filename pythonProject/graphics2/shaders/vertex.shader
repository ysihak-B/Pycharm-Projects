# version 330
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
layout(location = 2) in vec3 a_normal;

uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;
out vec2 v_texture;
out vec3 normal;
void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    normal = a_normal;
    v_texture = a_texture;
}