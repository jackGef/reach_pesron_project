import { Link } from 'react-router-dom'
import './header.css'

const Header = () => {
  return (
    <header>
        <nav>
            <Link className='link-class' to='/'>HOME</Link>
            <Link className='link-class' to='/ai/linearRegression'>Linear regression</Link>
            <Link className='link-class' to='/ai/logisticRegression'>Logistic Regression</Link>
        </nav>
    </header>
  )
}

export default Header
