# Templates

Templates help achieve this separation between presentation and business logic. In Flask, templates are written as separate files, stored in a templates folder that is inside the application package.

They keep the logic of your application separate from the layout or presentation of your web pages

The operation that converts a template into a complete HTML page is called rendering. To render the template I had to import a function that comes with the Flask framework called render_template(). This function takes a template filename and a variable list of template arguments, and returns the same template, but with all the placeholders in it replaced with actual values.

The render_template() function invokes the Jinja template engine that comes bundled with the Flask framework. Jinja substitutes {{ ... }} blocks with the corresponding values, given by the arguments provided in the render_template() call.

Jinja replaces placeholders with actual values during rendering, but this is just one of many powerful operations Jinja supports in template files. For example, templates also support control statements, given inside {% ... %} blocks

If the view function forgets to pass a value for the title placeholder variable, then instead of showing an empty title the template will provide a default one.

## Template inheriatance

Most web applications these days have a navigation bar at the top of the page with a few frequently used links, such as a link to edit your profile, to login, logout, etc. I can easily add a navigation bar to the index.html template with some more HTML, but as the application grows I will be needing this same navigation bar in other pages. I don't really want to have to maintain several copies of the navigation bar in many HTML templates, it is a good practice to not repeat yourself if that is possible.

Jinja has a template inheritance feature that specifically addresses this problem. In essence, what you can do is move the parts of the page layout that are common to all templates to a base template, from which all other templates are derived.