```
横向分割显示：
:vs filename
纵向分割显示：
:sp filename
关闭除光标所在的窗口之外的其他窗口：
:only

C v: block --> A(尾)/I(首) word-->Esc
V: line
v: point

ynw yy y$
dnd dd
```

```
" Vim Plugin
call plug#begin('~/.vim/plugged')
Plug 'morhetz/gruvbox'
Plug 'preservim/nerdtree'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'easymotion/vim-easymotion'
Plug 'preservim/nerdcommenter'
" Plug 'Yggdroot/LeaderF', { 'do': ':LeaderfInstallCExtension' }
call plug#end()

let mapleader = ";"
nnoremap <Leader>q :q<CR>
nnoremap <Leader>w :w<CR>
nnoremap <Leader>g :NERDTreeToggle<CR>
nnoremap <Leader>f :NERDTreeFind<CR>
nnoremap <Leader>h ^
nnoremap <Leader>l $
nnoremap <C-g> :set nohlsearch<CR>
nnoremap <C-i> :set ignorecase<CR>

set clipboard=unnamedplus    " 使用系统剪切版 -> Vim
set clipboard=unnamed      " Vim -> 系统剪切版
set hlsearch
set cursorline
set undofile
set history=1000
set relativenumber
set nu
set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4
" colorscheme gruvbox
autocmd vimenter * nested colorscheme gruvbox
set bg=dark

let g:EasyMotion_smartcase = 1
nmap f <Plug>(easymotion-s)

let g:NERDSpaceDelims = 1
```

