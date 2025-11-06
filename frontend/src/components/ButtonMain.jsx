import '../styles/ButtonMain.css';

// ButtonMain accepts either a `label` prop or children.
// Example usages:
// <ButtonMain label="Click me" />
// <ButtonMain>Click me</ButtonMain>
function ButtonMain({ label = null, children = null, ...rest }){
    const content = label ?? children;

    return(
        <button className="main-button" {...rest}>
            {content}
        </button>
    )
}

export default ButtonMain