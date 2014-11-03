if !has('python')
    finish
endif

function! SmartIdent()
    " TODO: remove the hardcoded PATH
    :python import sys, vim
    :python sys.argv = ['', vim.current.buffer.name]

    let s:script_folder_path = escape( expand( '<sfile>:p:h' ), '\' )
    let s:python_folder_path = s:script_folder_path . '/smartident.py'

    exe 'pyfile ' .  s:python_folder_path
endfunction

autocmd BufReadPost * :call SmartIdent()
