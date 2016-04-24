_ecli()
{
    local cur prev

    cur=${COMP_WORDS[COMP_CWORD]}
    prev=${COMP_WORDS[COMP_CWORD-1]}

    case ${COMP_CWORD} in
        1)
            COMPREPLY=($(compgen -W "cmd1 cmd2" ${cur}))
            ;;
        2)
            case ${prev} in
                cmd1)
                    COMPREPLY=($(compgen -W "foo" ${cur}))
                    ;;
                cmd2)
                    COMPREPLY=($(compgen -W "bar" ${cur}))
                    ;;
            esac
            ;;
        3)
            case ${prev} in
                foo)
                    COMPREPLY=($(compgen -W "do_thing" ${cur}))
                    ;;
                bar)
                    COMPREPLY=($(compgen -W "do_stuff" ${cur}))
                    ;;
            esac
            ;;
        *)
            COMPREPLY=()
            ;;
    esac
}

complete -F _ecli ecli\-nested
