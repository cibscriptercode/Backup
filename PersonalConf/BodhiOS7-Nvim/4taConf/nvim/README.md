# Mi Configuracíon básica para Neovim

## Descripción:
Configuración inicial de Neovim optimizada para trabajar con Python, con el objetivo de desarrollar un entorno de desarrollo integrado (IDE). Las siguientes instrucciones proporcionan una guía para instalar las herramientas y configuraciones necesarias para usar Neovim en sistemas GNU/Linux. Se han probado específicamente en Bodhi Linux, un sistema basado en Ubuntu, por lo que se espera que funcionen sin problemas en cualquier sistema basado en Debian.

Se recomienda encarecidamente utilizar una versión actualizada de Neovim para garantizar la compatibilidad con los plugins y las funcionalidades más recientes. Si algún comando de instalación falla o desea explorar otras opciones, le sugerimos que consulte la documentación oficial de Neovim y las fuentes relacionadas para obtener información actualizada y soluciones alternativas. Los enlaces proporcionados en estas instrucciones pueden servir como puntos de partida para acceder a la documentación oficial y a recursos adicionales.

## Pasos para instalar Neovim y utilizar esta configuración:

#### 1. Instalación de Homebrew:

<pre><code>sudo apt-get install build-essential procps curl file git unzip</code></pre>

<pre><code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code></pre>

<pre><code>test -d ~/.linuxbrew && eval "$(~/.linuxbrew/bin/brew shellenv)"
test -d /home/linuxbrew/.linuxbrew && eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
echo "eval \"\$($(brew --prefix)/bin/brew shellenv)\"" >> ~/.bashrc</code></pre>

<pre><code>brew --version</code></pre>

#### 2. Instalación de Neovim >= v0.9.5:

<pre><code>brew install neovim</code></pre>

#### 3. Instalación de una fuente Nerdfont:
Descarga una fuente, preferiblemente una fuente 'Mono'. Recomiendo la fuente 'VictorMono Nerd Font'. Luego, desde la carpeta de descarga, ejecuta:

<pre><code>sudo mv FuenteDescargada.zip /usr/share/fonts</code></pre>

<pre><code>cd /usr/share/fonts</code></pre>

<pre><code>sudo unzip FuenteDescargada.zip</code></pre>

<pre><code>fc-cache -f -v</code></pre>

#### 4. Cambia el tipo de letra y tamaño desde la configuración de tu terminal para que los cambios tomen efecto en Neovim.

#### 5. Instalación de Packer para la gestión de plugins:

<pre><code>git clone --depth 1 https://github.com/wbthomason/packer.nvim ~/.local/share/nvim/site/pack/packer/start/packer.nvim</code></pre>

#### 6. Instalación de dependencias para Telescope:

<pre><code>sudo apt-get install fd-find -y</code></pre>

<pre><code>sudo apt-get install ripgrep -y</code></pre>

#### 7. Instalación de nvm (Node Version Manager) y NodeJS, se recomienda instalar una versión LTS:

<pre><code>curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash</code></pre>

<pre><code>export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"</code></pre>

<pre><code>nvm ls-remote</code></pre>

<pre><code>nvm install vx.x.x</code></pre>

#### 8. Instalación de servidores para Lua, Python y Bash:

<pre><code>brew install lua-language-server</code></pre>

<pre><code>npm i -g pyright -y</code></pre>

<pre><code>npm i -g bash-language-server -y</code></pre>

#### 9. Clonar el repositorio de configuración:

<pre><code>cd ~/.config</code></pre>

<pre><code>git clone https://github.com/cibscripter/nvim.git</code></pre>

#### 10. Abrir el archivo de plugins para instalar plugins:

<pre><code>nvim ~/.config/nvim/lua/plugins.lua</code></pre>
Ejecutar en modo normal: <pre><code>:luafile %</code></pre> 
<pre><code>:PackerSync</code></pre>

#### 11. Finalmente, si ocurre algún error en la instalación de un plugin:
Navega a <i>~/.config/nvim/after/plugin/</i>, abre el archivo del plugin con el problema y ejecuta: <pre><code>:luafile %</code></pre>
Repite nuevamente el paso anterior.
