#include <windows.h>
#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <iostream>
using namespace std;

void framebuffer_size_callback(GLFWwindow* window, int width, int height); // resize call back function .. called whenever we resize the window
void processInput(GLFWwindow *window); // process user input .. called in the game loop

const unsigned int SCR_WIDTH = 800;
const unsigned int SCR_HEIGHT = 600;

int main()
{
    // initialize GLFW
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3); // opengl 3.3
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE); // core profile only


    GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "orfi -core gl", NULL, NULL);
    if (window == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate(); // clean up
        return -1;
    }
    glfwMakeContextCurrent(window); // make the window the current context in the current thread
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback); //  register the resize callback function

    // initialize Glad
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) // load opengl function pointers
    {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }

    // render loop
    while (!glfwWindowShouldClose(window))
    {
        // process input
        processInput(window); // check to see if the ESC key has been pressed

        //render
        glClearColor(0.27f, 0.27f, 0.45f, 1.0f); // clear the color buffer with this color
        glClear(GL_COLOR_BUFFER_BIT);

        // swap buffers and poll events
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    //clean up
    glfwTerminate();

    return 0;
}

void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
    glViewport(0, 0, width, height);
}

void processInput(GLFWwindow *window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
}
