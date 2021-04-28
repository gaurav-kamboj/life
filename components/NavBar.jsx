import React, { useState } from 'react';
import { useLocaleContext } from '@hooks/use-locale-context';
import Logo from './Logo';
import NavLink from './NavLink';
import LanguageSelector from './LanguageSelector';
import ThemeButton from './ThemeButton';
import useLocale from '@hooks/use-locale';
import {
    faDatabase,
    faHandsHelping,
    faHeart,
    faBookOpen,
    faBars,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const NavBar = () => {

    const { locale } = useLocaleContext()
    const t = useLocale(locale, 'home');

    const [isOpen, setIsOpen] = useState(false);

    const navLinks = [
        {
            icon: faBookOpen,
            title: `${t.learn}`,
            link: '/learn'
        },
        {
            icon: faHeart,
            title: `${t.campaigns}`,
            link: '/campaigns'
        },
        {
            icon: faHandsHelping,
            title: `${t.partnerWithUs}`,
            link: '/about#partner'
        },
        {
            icon: faDatabase,
            title: `${t.contributeData}`,
            link: '/data'
        },

    ]

    return (
        <section className="mb-20">
            <nav className="flex bg-gray-200 dark:bg-gray-1200 items-center justify-between px-5 py-2 fixed top-0 left-0 w-full z-50 md:shadow-sm">
                <div onClick={() => setIsOpen(prev => !prev)} className="flex items-center m-3 cursor-pointer md:hidden">
                    <FontAwesomeIcon icon={faBars} className="w-3" />
                </div>
                <a href="/" className="flex items-center m-3">
                    <Logo height={40} />
                    <h1 className="ml-1 uppercase font-black text-3xl text-gray-900 dark:text-gray-100">
                        {t.title}
                    </h1>
                </a>
                <div className="flex-1 flex items-center justify-end">
                    <div className="items-center justify-end hidden md:flex">
                        {
                            navLinks.map(({ icon, title, link }, id) =>
                                <NavLink key={id} title={title} link={link} icon={icon} />
                            )
                        }
                    </div>
                    <div className="flex items-center mx-4 mb-1">
                        <LanguageSelector />
                    </div>
                    <div className="flex items-center mx-4 mb-1">
                        <ThemeButton />
                    </div>
                </div>
            </nav>
            {
                isOpen &&
                <div className='flex bg-gray-200 dark:bg-gray-1000 py-2 flex-col items-center justify-center md:hidden px-4 mt-20'>
                    {
                        navLinks.map(({ icon, title, link }, id) =>
                            <NavLink key={id} title={title} link={link} icon={icon} />
                        )
                    }
                </div>
            }
        </section>
    );
}

export default NavBar;