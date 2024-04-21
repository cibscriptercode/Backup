# Mi configuración básica para Neovim.

<a href="https://neovim.io/">Neovim</a> es una versión moderna y mejorada del editor de texto Vim, diseñada para ofrecer una experiencia de edición más eficiente y extensible.

## Pasos para usar esta configuración:

<ol>
  <li>Instalar una versión actual de Neovim >= v0.9.5, recomiendo usar <a href="https://docs.brew.sh/Homebrew-on-Linux#install">Homebrew</a> para instalarlo en Linux.</li>
  <li>Instalar una versión LTS de <a href="https://nodejs.org/en">NodeJS</a>.</li>
  <li>(Opcional) Descargar e instalar una fuente tipo <i>'Mono'</i> desde <a href="https://www.nerdfonts.com/font-downloads">Nerd Fonts</a> y cambiar el tipo de letra desde la configuración de su terminal. </li>
  <li> Instalar <a href="https://github.com/wbthomason/packer.nvim?tab=readme-ov-file#quickstart">Packer</a> para la gestión de plugins.</li>
  <li>Clonar este repositorio en su directorio de configuración <code>cd ~/.config</code> con <code>git clone https://github.com/cibscripter/nvim.git</code></li>
  <li> Abrir el archivo de instalacion de plugins con <code>nvim ~/.config/nvim/lua/cibscripter_est/plugins.lua</code> y ejecutar <code>:PackerSync</code> en modo normal.
    <b>Nota:</b> Si aparece algún error al abrir este archivo, ignorar presionando la tecla ENTER hasta ingresar al archivo.
  </li> 
  <li>Puede instalar el autocompletado para su lenguaje de programación ingresando al editor y ejecutando por ejemplo <code>:CocInstall coc-pyright coc-sh coc-sql</code>. Consulte las opciones disponibles para <a href="https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions#implemented-coc-extensions">instalar</a>. Puede revisar las extensiones instaladas ejecutando <code>:CocList</code> en la opción <i>'extensions'</i>.</li>
</ol>

