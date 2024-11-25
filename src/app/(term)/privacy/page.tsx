import Image from "next/image";
import React from "react";
import color_hunt_logo_animation_gif from "@/app/photos/color-hunt-logo-animation.gif";

export default function Term() {
  return (
    <div
      className={`flex flex-col justify-center items-center gap-10 *:*:p-2 px-5`}
    >
      <Image
        src={color_hunt_logo_animation_gif}
        alt={`color-hunt-logo-animation.gif`}
        className={`w-52  object-cover`}
      />
      <div>
        <h1 className={`text-center font-bold`}>Privacy Policy</h1>
        <p>
          This is Color Hunt&apos;s Privacy Policy for www.colorhunt.co. This
          document explains Color Hunt policies for the collection, use, and
          disclosure of personal information on www.colorhunt.co.This privacy
          policy deals with personally-identifiable information (referred to as
          &quot;data&quot; below) that may be collected by this site.
        </p>
      </div>
      <div>
        <h1 className={`text-center font-bold`}>COLLECTION OF DATA</h1>
        <p>
          As on many websites, the site editor may automatically receive general
          information that is contained in server log files, such as your IP
          address, and cookie information. Information about how advertising may
          be served on this site (if it is indeed the site editor&apos;s policy to
          display advertising) is set forth below.
        </p>
      </div>
      <div>
        <h1 className={`text-center font-bold`}>USE OF DATA</h1>
        <p>
          Data may be used to customize and improve your user experience on this
          site. Efforts will be made to prevent your data from being made
          available to third parties unless provided for otherwise in this
          Privacy Policy; your consent is obtained, such as when you choose to
          opt-in or opt-out for the sharing of data; a service provided on our
          site requires interaction with a third party, or is provided by a
          third party, such as an application service provider; (iv) pursuant to
          legal action or law enforcement; it is found that your use of this
          site violates the site editor&apos;s policy, terms of service, or
          other usage guidelines, or if it is deemed reasonably necessary by the
          site editor to protect the site editor&apos;s legal rights and/or
          property; or this site is purchased by a third party, in which case
          that third party will be able to use the data in the same manner as
          set forth in this policy.
        </p>
        <p>
          In the event you choose to use links displayed on this website to
          visit other websites, you are advised to read the privacy policies
          published on those sites. Color Hunt uses third-party advertising
          companies to serve ads when you visit our website. These companies may
          use information (not including your name, address, email address, or
          telephone number) about your visits to this and other websites in
          order to provide advertisements about goods and services of interest
          to you.
        </p>
      </div>
      <div>
        <h1 className={`text-center font-bold`}>COOKIES</h1>
        <p>
          Like many websites, this website sets and uses cookies to enhance your
          user experience — to remember your personal settings, for instance.
          Advertisements may display on this website and, if so, may set and
          access cookies on your computer; such cookies are subject to the
          privacy policy of the parties providing the advertisement. However,
          the parties providing the advertising do not have access to this
          site&apos;s cookies. These parties usually use non-personally-identifiable
          or anonymous codes to obtain information about your visits to this
          site.
        </p>
        <p>
          Please note that turning off advertising cookies won’t mean that you
          are not served any advertising, merely that it will not be tailored to
          your interests.
        </p>
      </div>
      <div>
        <h1 className={`text-center font-bold`}>Changes to Terms of Service</h1>
        <p>
          We reserve the right, at our sole discretion, to modify or replace
          these Terms of Service at any time. Your continued use of our website
          after any such changes constitutes your acceptance of the new Terms of
          Service.
        </p>
      </div>
    </div>
  );
}
