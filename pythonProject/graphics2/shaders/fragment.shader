# version 330
in vec2 v_texture;
in vec3 normal;

out vec3 outNormal;
out vec4 outColor;
uniform sampler2D s_texture;
void main()
{
//     outNormal = vec4(normal, 1.0);
    outColor = texture(s_texture, v_texture);
}