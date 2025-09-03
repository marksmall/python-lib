from setuptools import find_packages, setup

setup(
    name="flake8-dsp",
    version="0.1.0",
    description="Custom Flake8 plugins for DSP coding standards.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "flake8.extension": [
            "NLB100 = plugins.newline_after_block:NewlineAfterBlockChecker",
            "NCP100 = plugins.none_comparison:NoneComparisonChecker",
            "BEX100 = plugins.bare_except:BareExceptChecker",
            "MD100 = plugins.mutable_default:MutableDefaultChecker",
            "ERT100 = plugins.explicit_return_type:ExplicitReturnTypeChecker",
            "NP100 = plugins.no_print:NoPrintChecker",
        ],
    },
)
